from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import twitter_module
from twitter_module import run_twitter
from django.http import HttpResponse
import json
import time


def first(request):
    return render(request,'twitterrunning.html')
    #return render(request,'index.html',{'posts':post})	

def second(request):
    if request.method == "POST" :
        post = PostForm(request.POST)
        name=request.POST['your_query_1']

        time_period_1=request.POST['your_query_2']
        if time_period_1 == '':
            time_period_1 = 20
        time_period=int(time_period_1)
        if time_period > 60 or time_period < 0:
            time_period = 20
        tweet, positive_sentiment, negative_sentiment=run_twitter(name)
        time.sleep(time_period)
        return render(request,'display_result.html',{'query':name,'pos':tweet,'positive_counter':positive_sentiment,'negative_counter':negative_sentiment,'time_limit':time_period,'length_of_list':len(tweet)})
    return render(request,'display_result.html')