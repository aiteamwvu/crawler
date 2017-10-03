import json, time, feedparser, schedule, config, threading, pymongo
from dateutil.parser import parse
from neo4j.v1 import GraphDatabase, basic_auth

class Crawler:
	conn_mongo = None
	conn_neo4j = None
	debug = True

	def get_neo4j(self):
		if self.conn_neo4j:
			return self.conn_neo4j.session()
		self.conn_neo4j = GraphDatabase.driver(config.neo4j_host, auth=basic_auth(config.neo4j_user, config.neo4j_pass))
		return self.conn_neo4j.session()

	def get_mongo(self):
		if self.conn_mongo:
			return self.conn_mongo
		self.conn_mongo = pymongo.MongoClient()[config.mongo_db]
		return self.conn_mongo

	def extract(self, callback=None):
		for source in config.sources:
			feed = feedparser.parse(source["source_url"])
			for entry in feed["entries"]:
				article = json.loads(json.dumps(entry, default=str))
				article.update(source)
				article["_id"] = article["link"]
				if "published" in article:
					article["timestamp"] = int(time.mktime(parse(article["published"]).timetuple()))
				elif "updated" in article:
					article["timestamp"] = int(time.mktime(parse(article["updated"]).timetuple()))
				if self.debug:
					print(json.dumps(article, indent=4, sort_keys=True))
				if callback:
					callback(article, source["source_table"])

	def extract_and_save(self):
		self.extract(self.insert_all)

	def insert_all(self, value, table="Node"):
		self.insert_mongo(value, table)
		self.insert_neo4j(value, table)

	def insert_neo4j(self, value, table="Node"):
		labels = ["author_detail", "summary_detail", "title_detail", "subtitle_detail", "source"]
		for label in labels:
			if label in value:
				for i in value[label]:
					if value[label][i] is not None:
						value[label + "_" + i] = value[label][i]
				del value[label]
		labels = ["tags", "links", "content", "authors", "media_content", "media_thumbnail"]
		for label in labels:
			if label in value:
				for obj in value[label]:
					for j in obj:
						index =label + "_" + j
						if index not in value:
							value[index] = []
						if obj[j] is not None:
							value[index].append(obj[j])
				del value[label]
		try:
			self.get_neo4j().run(statement=("CREATE (x:%s) SET x = {value}" % (table)), parameters={'value': value})
			print("INSERTED")
			labels = ["tags_term", "source_categories"]
			for label in labels:
				query = """
				MATCH (f:%s {_id:"%s"})
				UNWIND f.%s as value
				MATCH (a) WHERE ANY(item IN a.%s WHERE item =~ value AND a._id <> "%s")
				CREATE (f)-[:%s {%s: value}]->(a)
				""" % (table, value["_id"], label, label, value["_id"], label.upper(), label)
				self.get_neo4j().run(statement=query)
				print("LINKED")
		except Exception as e:
			if "already exists" not in str(e):
				print(json.dumps(value, indent=4, sort_keys=True))
				print(e)

	def insert_mongo(self, value, table="Node"):
		self.get_mongo()[table].save(value)

	def start_cron(self):
		threading.Thread(target=self.cron).start()

	def cron(self):
		schedule.every(config.time).minutes.do(self.extract_and_save)
		while True:
			schedule.run_pending()
			time.sleep(1)

crawler = Crawler()
#crawler.extract()
crawler.extract_and_save()
crawler.start_cron()
