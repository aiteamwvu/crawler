import json, time, feedparser, schedule

def get_config():
	with open("config.json") as json_data:
		return json.load(json_data)
	raise

def extract():
	config = get_config()
	for source in config["sources"]:
		print(source["name"])
		feed = feedparser.parse(source["url"])
		for entry in feed["entries"]:
			print(entry["title"])

def cron():
	config = get_config()
	schedule.every(config["time"]).minutes.do(extract)
	while True:
		schedule.run_pending()
		time.sleep(1)

def init():
	extract()
	cron()

init()