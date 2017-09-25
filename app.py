import json, time, feedparser, schedule, config, threading, pymongo
from neo4j.v1 import GraphDatabase, basic_auth

class Crawler:
	conn = None

	def get_neu4j(self):
		if self.conn:
			return self.conn.session()
		self.conn = GraphDatabase.driver(config.neo4j_host, auth=basic_auth(config.neo4j_user, config.neo4j_pass))
		return self.conn.session()

	def get_mongo(self):
		if self.conn:
			return self.conn
		self.conn = pymongo.MongoClient()[config.mongo_db]
		return self.conn

	def extract(self, callback=None):
		for source in config.sources:
			feed = feedparser.parse(source["source_url"])
			for entry in feed["entries"]:
				article = json.loads(json.dumps(entry, default=str))
				article.update(source)
				article["_id"] = article["link"]
				print(json.dumps(article, indent=4, sort_keys=True))
				if callback:
					callback(article, source["source_table"])

	def extract_and_save(self):
		self.extract(self.insert_mongo)

	def insert_neo4j(self, value, table="Node"):
		self.get_neu4j().run(statement="CREATE (x:Article) SET x = {value}", parameters={'table': table, 'value': value})

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
crawler.extract()
#crawler.extract_and_save()
#crawler.start_cron()