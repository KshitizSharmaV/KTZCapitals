# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import urllib2
# Create your views here.

def first(request):
	url="http://pib.nic.in/newsite/erelease.aspx?relid=0"
	page = urllib2.urlopen(url).read()
	soup=bs(page)
	buletin=[]

	all_news= soup.findAll("li", class_= "rel")
	for news in all_news:
		add=news.text
		add = unicode(add).replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
		buletin.append(add)
	return render(request,'politics.html',{'buletin':buletin})