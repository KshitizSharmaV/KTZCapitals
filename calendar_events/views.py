# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib
import re


def first(request):
	upcoming_company_results={}
	date={}
	r=urllib.urlopen('http://www.bseindia.com/corporates/Forth_Results.aspx?expandable=0').read()
	soup=BeautifulSoup(r)
	companies= soup.findAll("tr", class_= "TTRow")
	i=0
	for company in companies:
		upcoming_company_results[i]=str(company.find("td",class_="TTRow_left").text)
		date[i]= str(company.contents[3].text)
		i=i+1
	return render(request,'calendar_templates.html',{'upcoming_company_results':upcoming_company_results,'date':date})