# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse

from google_trend_module import value_analysis
from google_trend_module import get_trending_data
from .forms import PostForm

def first(request):
	return render(request,'googletrends_display.html')

def second(request):
	if request.method == "POST":
		post = PostForm(request.POST)
        name=request.POST['your_google_query']
        if name=="":
        	return render(request,'googletrends_display.html',{'message':"Action Not Allowed"})
	trendingdata=get_trending_data()
	#interest_over_time_df, interest_by_region_df=value_analysis(a)
	financial_markets=['BSESN','Nifty50','S&P 500','DJIA','Nasdaq',' Russell 2000 ','Nikkei 225 ','Shanghai Composite']
	politics=['Donald Trump','Narendar Modi','Shushma Swaraj','Benjamin Netanyahu','Park Geun-hye',' Ali Khamenei','Dilma Rousseff','Shinzo Abe','Francois Hollande','David Cameron','Pope Francis','Angela Merkel','Vladimir Putin','Xi Jinping','Barack Obama']
	return render(request,'googletrends.html',{'trendingdata':trendingdata,'name':name,'politic':politics,'financial_markets':financial_markets})
	#return render(request,'googletrends.html',{'interest':interest_over_time_df,'region':interest_by_region_df})
