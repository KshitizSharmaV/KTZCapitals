# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from django.shortcuts import render
from forex_python.converter import CurrencyRates,CurrencyCodes


def first(request):
	return render(request,'forex_template.html')

def currency_convertor(request):
	c = CurrencyRates()
	s=CurrencyCodes()
	currency_list={'USD','EUR','JPY','GBP','AUD','CAD','CHF','CNY','SEK','NZD','MXN','SGD','HKD','INR'}
	if request.method == "POST" :
		trade_size1_3 =request.POST['trade_size1_3']
		if trade_size1_3 is '':
			trade_size1_3=1
		else:
			trade_size1_3=float(trade_size1_3)	
		cur_1=request.POST['sel1_1']
		cur_2=request.POST['sel1_2']
		if cur_2 == cur_1:
			cur_2='INR'
			cur_1='USD'
		symbol=s.get_symbol(cur_2)
		rate=c.get_rate(cur_1,cur_2)
		value=rate*trade_size1_3
		one=1
		return render(request,'currency_convertor.html',{'currencyList':currency_list,'value':value,'symbol':symbol,'from_currency':cur_1,'to_currency':cur_2,'rate':rate,'one':one})
	return render(request,'currency_convertor.html',{'currencyList':currency_list})	

def margin(request):
	c = CurrencyRates()
	s=CurrencyCodes()
	leverage={1,0.5}
	currency_list={'GBP','AUD','CAD','CHF','CNY','SEK','NZD','MXN','SGD','HKD','INR','USD','EUR','JPY'}
	if request.method == "POST" :
		margin=0
		base_currency= request.POST['sel4_1']
		counter_currency= request.POST['sel4_2']
		account_currency= request.POST['sel4_3']
		leverage=float(request.POST['sel4_4'])
		print leverage
		trade_size4_5 =request.POST['trade_size4_5']
		if trade_size4_5 is '':
			trade_size4_5=10000
		else:
			trade_size4_5=float(trade_size4_5)

		if base_currency == account_currency:
			mp=1.0
		else:
			mp=c.get_rate(base_currency,account_currency)
			
		symbol=s.get_symbol(counter_currency)		
		margin=(trade_size4_5 * leverage) * mp
		
		return render(request,'margin.html',{'symbol':symbol,'currencyList':currency_list,'margin':margin,'base_currency':base_currency,'counter_currency':counter_currency,'account_currency':account_currency,'mp':mp})		
	return render(request,'margin.html',{'currencyList':currency_list,'leverage':leverage})	

def pip(request):
	c = CurrencyRates()
	s=CurrencyCodes()
	decimal=0.0001
	currency_list={'GBP','AUD','CAD','CHF','CNY','SEK','NZD','MXN','SGD','HKD','INR','USD','EUR','JPY'}
	if request.method == "POST" :
		pip=0
		base_currency= request.POST['sel2_1']
		counter_currency= request.POST['sel2_2']
		account_currency= request.POST['sel2_3']
		trade_size2_4 =request.POST['trade_size2_4']
		if trade_size2_4 is '':
			trade_size2_4=10000
		else:
			trade_size2_4=float(trade_size2_4)

		if counter_currency == account_currency:
			mp=1.0
		else:
			mp=c.get_rate(account_currency,counter_currency)
			
		if (base_currency == 'JPY')	or (counter_currency == 'JPY'):
			decimal=0.01
		symbol=s.get_symbol(counter_currency)		
		pip=(decimal * trade_size2_4)/mp
		
		return render(request,'pip.html',{'symbol':symbol,'currencyList':currency_list,'pip':pip,'base_currency':base_currency,'counter_currency':counter_currency,'account_currency':account_currency,'mp':mp})		
	return render(request,'pip.html',{'currencyList':currency_list})	
	
def sandl(request):
	currency_list={'AUD','CAD','CHF','CNY','SEK','NZD','SGD','HKD','INR','USD','EUR','JPY','GBP','MXN'}
	return render(request,'sandl.html',{'currencyList':currency_list})	
	