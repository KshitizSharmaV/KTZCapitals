# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import urllib2
from nsepy import get_history, get_index_pe_history

# Create your views here.
def first(request):
	url="http://www.moneycontrol.com/stocks/marketstats/fii_dii_activity/"
	
	#url="http://www.moneycontrol.com/stocks/marketstats/activity.php?flag=FII"
	page = urllib2.urlopen(url).read()
	soup=bs(page)

	#Extract Debt Data Per Day and last 12 months
	gross=[]
	gross_day=[]
	gross_month=[]
	fii=[]
	dii=[]
	dii_gross_day=[]
	dates=[]
	datelist_day=[]
	datelist_month=[]
	dates=soup.findAll("a", {'style':"color:#333"})
	
	for i in range(29):
		if i<5:
			datelist_day.append(dates[i].text)
		else:
			datelist_month.append(dates[i].text)	
	
	grosses=soup.findAll("span",{'class':['red_13', 'grn_13']})
	for i in range(70):
		if i % 2 ==0:
			fii.append(float(grosses[i].text.replace(',','')))
		else:
			dii.append(float(grosses[i].text.replace(',','')))	
	
	for i in range(29):
		if i<5:
			gross_day.append(fii[i])
		else:
			gross_month.append(fii[i])	


	for i in range(5):
		if i<5:
			dii_gross_day.append(dii[i])

	
	fii_last=fii[0]	
	dii_last=dii[0]	
	#Extract Debt Data Per Day and last 12 months
	zipped=zip(datelist_month,gross_month)
	return render(request,'fii.html',{'dii_last':dii_last,'fii_last':fii_last,'dii_gross_day':dii_gross_day,'zipped':zipped,'gross_day':gross_day,'gross_month':gross_month,'datelist_day':datelist_day,'datelist_month':datelist_month,'first_1':"FII Forign Institutional Investors", 'second_2':"Equity Debt Sold Buy", 'third_3':"Inflow of Foregin Investment", 'fourth_4':"FII and FDI Data",'fifth_5':"FII Influence Indian Markets",'sixth_6':"FII past data"})







