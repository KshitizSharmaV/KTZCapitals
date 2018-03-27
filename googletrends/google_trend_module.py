from pytrends.request import TrendReq
from bs4 import BeautifulSoup as bs
import urllib2

def value_analysis():
	google_username = "karansharmav@gmail.com"
	google_password = "kingpawns"
	path=""
	print "hello begin please"
	pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
	# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
	pytrend.build_payload(kw_list=['OPEC'],timeframe='now 7-d')
	# Interest Over Time
	interest_over_time_df = pytrend.interest_over_time()
	print interest_over_time_df

	interest_by_region_df = pytrend.interest_by_region()
	print interest_by_region_df
	#trending_searches=pytrend.trending_searches()

	#return(trending_searches)

def get_trending_data():
	url = "http://pulse.zerodha.com"
	num=0
	page = urllib2.urlopen(url).read()

	soup = bs(page)
	trendingText = []
	trendingLinks= soup.findAll("a", class_= "word")
	for trending in trendingLinks:
		trendingText.append(str(trending.text))
	return(trendingText)
