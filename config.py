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
}, {
    "source_table": "Article",
	"source_name": "Tech Mobile Computing",
	"source_url": "http://www.techradar.com/rss/news/mobile-computing",
	"source_content": "text",
	"source_categories": ["Mobile Computing"]
}, {
    "source_table": "Article",
	"source_name": "Tech Advisor",
	"source_url": "http://www.techadvisor.co.uk/feature/rss",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "WSJ Tech",
	"source_url": "http://www.wsj.com/xml/rss/3_7455.xml",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "NYT Personal Tech",
	"source_url": "http://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "NYT General Tech",
	"source_url": "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "Life Hacker",
	"source_url": "http://lifehacker.com/rss",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "Android Central",
	"source_url": "http://feeds2.feedburner.com/androidcentral",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "9 to 5 Google",
	"source_url": "https://9to5google.com/feed/",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "Mac Rumors",
	"source_url": "http://feeds.macrumors.com/MacRumors-All",
	"source_content": "text",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "ZDNet",
	"source_url": "http://www.zdnet.com/videos/rss.xml",
	"source_content": "videos",
	"source_categories": ["general"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic Artificial Intelligence",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/artificial-intelligence/",
	"source_content": "text",
	"source_categories": ["Artificial Intelligence"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic Big Data",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/big-data/",
	"source_content": "text",
	"source_categories": ["Big Data"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic Digital Transformation",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/digital-transformation/",
	"source_content": "text",
	"source_categories": ["Digital Transformation"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic E-Commerce",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/e-commerce/",
	"source_content": "text",
	"source_categories": ["Digital E-Commerce"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic Internet of Things",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/internet-of-things/",
	"source_content": "text",
	"source_categories": ["Digital Internet of Things"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic Virtualization",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/virtualization/",
	"source_content": "text",
	"source_categories": ["Digital Virtualization"]
}, {
    "source_table": "Article",
	"source_name": "Tech Republic Cloud",
	"source_url": "https://www.techrepublic.com/rssfeeds/topic/cloud/",
	"source_content": "text",
	"source_categories": ["Digital Cloud"]
}]
