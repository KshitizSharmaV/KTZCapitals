# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import urllib2


# Create your views here.

def first(request):
	return render(request,'commodity_markets.html')

def mcx(request):
	return HttpResponse(likes)

def ncdex(request):
	likes=10
	return HttpResponse(likes)