# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import urllib2
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def industries(request):
	return render(request,'industries.html')
	

def sector_gdp(request):
	url="http://statisticstimes.com/economy/sectorwise-gdp-contribution-of-india.php"
	page = urllib2.urlopen(url).read()
	soup=bs(page)
	industry_names={}
	sector_name=[]
	sector_percent=[]
	subsector_name=[]
	subsector_percent=[]
	industry_names=soup.find("tbody")
	#industry_data=soup.findAll("td",class="_data")
	industry_heading=industry_names.findAll("tr",{'style':"background-color:#B2F0D1"})
	industry_subparts=industry_names.findAll("tr",attrs={'style':None})
	
	for sectors in industry_heading:
		sector_name.append(str(sectors.contents[2].text))
		#sector_name[i]=str(sectors.find("td",attrs={'class':"name",'style':None}).text)
		sector_percent.append(sectors.contents[9].text)
		
	sector=zip(sector_name,sector_percent)
	print sector
	
	
	for sectors in industry_subparts:
		subsector_name.append(str(sectors.contents[1].text))
		subsector_percent.append(sectors.contents[8].text)
		
	sub_sector=zip(subsector_name,subsector_percent)
	print sub_sector
	return render(request,'sector_gdp.html',{'sector':sector,'sub_sector':sub_sector})


def sector_performance(request):
	if request.method == "POST" :	
		text1 = str(request.POST.get('iid'))
		urls={"Bt1":"http://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/year-to-date.html",
		"Bt2":"http://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/half-year-to-date.html",
		"Bt3":"http://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/month-to-date.html",
		"Bt4":"http://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/today.html"}
		url=urls[text1]
	else:
		url="http://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/year-to-date.html"	
	print url	
	page=urllib2.urlopen(url).read()
	soup=bs(page)
	sectors={}
	sector_percent_without_symbol=[]
	sector_namess=[]
	sector_market_cap=[]
	sector_percent=[]
	sector_name=soup.findAll("tr",class_="trgr")
	i=0
	for sector in sector_name:
		sector_market_cap.append(sector.contents[3].text)
		sector_percent_without_symbol.append(float(sector.find("td",attrs={'width':"85",'class':['grn', 'rd']}).text.replace('%','')))
		sector_namess.append(sector.contents[1].text)
	
	results=zip(sector_namess,sector_market_cap,sector_percent_without_symbol)
	print results
	return render(request,'sector_performance.html',{'sector_performance':results})




