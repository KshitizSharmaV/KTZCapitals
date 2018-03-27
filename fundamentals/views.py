# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
from django.shortcuts import render
import math


def first(request):
	return render(request,'fundamentals_home.html')

def fifth(request):
	try:	
		if request.POST.get("vod"):
			interest_rate=float(request.POST['interest_rate'])
			face_value=float(request.POST['face_value'])
			maturity=float(request.POST['maturity'])
			n=float(request.POST['n'])
			rate_of_return=float(request.POST['rate_of_return'])
			PVIF=1/math.pow((1+rate_of_return/100),n)
			PVIFA=(1-PVIF)/(rate_of_return/100)
			interest=(interest_rate/100)*face_value
			vd=round(interest*PVIFA + maturity*PVIF,2)
			return render(request,'vob.html',{'interest_rate':interest_rate,'maturity':maturity,'PVIF':PVIF,'n':n,'vd':vd,'PVIFA':PVIFA,'face_value':face_value,'rate_of_return':rate_of_return})
	except ValueError:
		return render(request,'error_file.html')		
	return render(request,'vob.html')	
	





def fourth(request):
	try:
		if request.POST.get("voe"):
			dividend_4=float(request.POST['dividend_4'])
			face_value_4=float(request.POST['face_value_4'])
			dividend_rate_4=float(request.POST['dividend_rate_4'])
			current_share_price_4= float(request.POST['current_share_price_4'])
			rate_of_return_4=float(request.POST['rate_of_return_4'])
			print rate_of_return_4-dividend_rate_4
			v=round((dividend_4/(rate_of_return_4-dividend_rate_4))*100,2)
			if v < current_share_price_4:
				Suggestion_4="Share is overvalued don't buy"
			else:
				Suggestion_4="Share can be bought"
			return render(request,'voe.html',{'rate_of_return_4':rate_of_return_4,'current_share_price_4':current_share_price_4,'dividend_4':dividend_4,'face_value_4':face_value_4,'dividend_rate_4':dividend_rate_4,'Suggestion_4':Suggestion_4,'v':v})

		if request.POST.get("voe_2"):
			no_of_equity_shares=float(request.POST['no_of_equity_shares'])
			face_value_of_equity_shares=float(request.POST['face_value_of_equity_shares'])
			profit_after_tax=float(request.POST['profit_after_tax'])
			retention_ratio= float(request.POST['retention_ratio'])
			worth_of_equity_shares=float(request.POST['worth_of_equity_shares'])
			required_rate_of_return=float(request.POST['required_rate_of_return'])
			eps=profit_after_tax/no_of_equity_shares
			worth_per_share= worth_of_equity_shares/no_of_equity_shares
			print eps
			print worth_per_share
			roe=(eps/worth_per_share)
			print roe
			g=((1- retention_ratio/100)*(roe))*100
			print g
			D0=(retention_ratio/100)*(eps)
			print D0
			D1=D0+(g*D0/100)
			print D1
			Ve=round((D1/(required_rate_of_return-g))*100,2)
			return render(request,'voe.html',{'g':g,'Ve':Ve})
	except ValueError:
		return render(request,'error_file.html')	
	return render(request,'voe.html')







def third(request):
	try:
		if request.POST.get("vops"):
			dividend_rate_3=float(request.POST['dividend_rate_3'])
			face_value_3=float(request.POST['face_value_3'])
			maturity_3=float(request.POST['maturity_3'])
			n_3=float(request.POST['n_3'])
			rate_of_returns=float(request.POST['rate_of_return_3'])
			print rate_of_returns
			PVIF_3=1/math.pow((1+rate_of_returns/100),n_3)
			PVIFA_3=(1-PVIF_3)/(rate_of_returns/100)
			interest_3=(dividend_rate_3/100)*face_value_3
			vops_3=round(interest_3*PVIFA_3 + maturity_3*PVIF_3,2)
			return render(request,'vop.html',{'rate_of_returns':rate_of_returns,'maturity_3':maturity_3,'PVIF':PVIF_3,'n_3':n_3,'vops_3':vops_3,'PVIFA':PVIFA_3,'face_value_3':face_value_3,'dividend_rate_3':dividend_rate_3})			
	except ValueError:
		return render(request,'error_file.html')	
	return render(request,'vop.html')


def second(request):
	try:
		if request.POST.get("ytm"):
			cr=float(request.POST['cr'])
			R1=request.POST['R1']
			FV=float(request.POST['FV'])
			if R1 == '':
				R1 = float((cr/100)*FV)
			else:
				R1=float(R1)

			P=request.POST['P']

			if P == '':
				P=float(FV)
			else:
				P=float(P)

			cgt=request.POST['cgt']
			nt=request.POST['nt']
			if  nt != '':
				nt=float(nt)
				R1=R1-(nt/100)*R1
				


			M=request.POST['M']

			if M == '':
				M=float(FV)
			else:
				M=float(M)

			if cgt != '':
				cgt=float(cgt)
				M= M - ((M-P)*cgt)/100
			n=float(request.POST['n'])

			ytm1=(R1+(M-P)/n)
			ytm2=(M+P)/2
			ytm=round((ytm1/ytm2)*100,2)
			return render(request,'ytm.html',{'R1':R1,'M':M,'P':P,'n':n,'ytm':ytm,'cr':cr,'FV':FV,'cgt':cgt,'nt':nt})	
	except ValueError:
		return render(request,'error_file.html')	
	return render(request,'ytm.html')		