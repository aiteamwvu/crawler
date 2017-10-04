time = 1
neo4j_host = "bolt://localhost:7687"
neo4j_user = "neo4j"
neo4j_pass = "edupassword"
mongo_db = "test"
sources = [{
    "source_table": "Article",
	"source_name": "Futurism",
	"source_url": "https://futurism.com/feed/",
	"source_content": "text",
	"source_categories": ["future"]
}, {
    "source_table": "Article",
	"source_name": "TechCrunch Gadgets",
	"source_url": "http://feeds.feedburner.com/crunchgear",
	"source_content": "text",
	"source_categories": ["gadgets"]
}, {
    "source_table": "Article",
	"source_name": "Wired Gadgets",
	"source_url": "https://www.wired.com/feed/category/gear/latest/rss",
	"source_content": "text",
	"source_categories": ["gadgets"]
}, {
    "source_table": "Article",
	"source_name": "Tech Radar Software",
	"source_url": "http://www.techradar.com/rss/news/software",
	"source_content": "text",
	"source_categories": ["software"]
}, {
    "source_table": "Article",
	"source_name": "CNET Videos",
	"source_url": "http://feed.cnet.com/feed/podcast/all/hd.xml",
	"source_content": "video",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "IEEE Spectrum Videos",
	"source_url": "https://spectrum.ieee.org/rss/videos",
	"source_content": "video",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "Slashdot Developers",
	"source_url": "http://rss.slashdot.org/Slashdot/slashdotDevelopers",
	"source_content": "text",
	"source_categories": ["developer"]
}, {
    "source_table": "Article",
	"source_name": "Tech Radar Internet",
	"source_url": "http://www.techradar.com/rss/news/internet",
	"source_content": "text",
	"source_categories": ["Internet"]
}]
