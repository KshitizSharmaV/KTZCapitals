# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse

def topfile(request):
    return render(request,'index.html')
def zero(request):
    return render(request,'file0.html')
def one(request):
    return render(request,'file1.html')
def two(request):
    return render(request,'file2.html')
def three(request):
    return render(request,'file3.html')
def four(request):
    return render(request,'file4.html')
def five(request):
    return render(request,'file5.html')
def six(request):
    return render(request,'file6.html')
def seven(request):
    return render(request,'file7.html')
def eight(request):
    return render(request,'file8.html')
def nine(request):
    return render(request,'file9.html')
def ten(request):
    title="Jobs of brokers in financial markets"
    return render(request,'file10.html',{'title':title })  

def twelve(request):
    title="Bitcoin a bubble or new gold"
    return render(request,'file12.html',{'title':title, 'first_1':"Bitcoin", 'second_2':"cryptocurrency", 'third_3':"Ethereum", 'fourth_4':"Digital Currency",'fifth_5':"Miners"})    

def thirteen(request):
    title="Gulf Crisis and it's impact!!"
    return render(request,'file13.html',{'title':title,'first_1':"Gulf crisis", 'second_2':"UAE Iran Egypt", 'third_3':"Fifa 2020", 'fourth_4':"Liquified Natural Gas (LNG)",'fifth_5':"Food crisis Energy"})

def fourteen(request):
    title=" Goods And Service Tax (GST) "
    return render(request,'file14.html',{'title':title,'first_1':"GST",'second_2':"Indian Government GST"})

def main1(request):
    return render(request,'Main1.html',{'title':"KTZ Capitals",'first_1':"About KTZ Capitals",'second_2':"Financial Services",'third_3':"Kshitiz Sharma",'fourth_4':"KTZ Capitals Sharma"})
def main2(request):
    return render(request,'Main2.html',{'title':" Application and Software",'first_1':"Twitter Analysis",'second_2':"News Analysis",'third_3':"Forex, Pip, margin calculator",'fourth_4':"Economic Calendar"})    
def main5(request):
    return render(request,'Main5.html')
def main4(request):
    return render(request,'Main4.html',{'title':"Algorithmic Trading",'first_1':"Moving Averages",'second_2':"Arbitrage",'third_3':"Custom Algorithms trading",'fourth_4':" technical indicators coding"})
def main6(request):
    return render(request,'Main6.html',{'title':"News Information and Data Provider",'first_1':"Python Libraries For finance",'second_2':"Data for finance",'third_3':"Financial data for free",'fourth_4':" News and financial news"})    
def main7(request):
    return render(request,'Main7.html',{'title':"Technology and Innovation"})    


      

'''def search_result(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})'''


