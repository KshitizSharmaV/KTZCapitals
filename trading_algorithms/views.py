# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def market_neutral_strategy(request):
	return render(request,'market_neutral_strategy.html',{'first_1':"Market Neutal KTZ Capitals",'second_2':"Market Neutal Algorithm",'third_3':"Market Neutal Trading",'fourth_4':"Market Neutal Working Softwares"})

def mean_reversion_algorithm(request):
	return render(request,'mean_reversion_algorithm.html',{'first_1':"KTZ capitals mean Reversion Algorith",'second_2':"Mean Reversion Algorithm Trading",'third_3':"Mean Reversion Softwares"})
	
def black_scholes(request):
	return render(request,'black_scholes.html',{'first_1':"KTZ Capitals Black Scholes Model","second_2":"Black Scholes Algorithm"})