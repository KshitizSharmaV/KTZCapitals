from django.conf.urls import url
from data import views

urlpatterns = [
	url(r'^$', views.topfile, name="topfile"),
    url(r'^file0.html/$', views.zero, name="zero"),
    url(r'^file1.html/$', views.one, name="one"),
    url(r'^file2.html/$', views.two, name="two"),
    url(r'^file3.html/$', views.three, name="three"),
    url(r'^file4.html/$', views.four, name="four"),
    url(r'^file5.html/$', views.five, name="five"),
    url(r'^file6.html/$', views.six, name="six"),
    url(r'^file7.html/$', views.seven, name="seven"),
    url(r'^file8.html/$', views.eight, name="eight"),
    url(r'^file9.html/$', views.nine, name="nine"),
    url(r'^file10.html/$', views.ten, name="ten"),
    url(r'^file12.html/$', views.twelve, name="twelve"),
    url(r'^file13.html/$', views.thirteen, name="thirteen"),
    url(r'^file14.html/$', views.fourteen, name="fourteen"),
    url(r'^Main1.html/$', views.main1, name="main1"),
    url(r'^Main2.html/$', views.main2, name="main2"),
    url(r'^Main4.html/$', views.main4, name="main4"),
    url(r'^Main5.html/$', views.main5, name="main5"),
    url(r'^Main6.html/$', views.main6, name="main6"),
    url(r'^Main7.html/$', views.main7, name="main7"),
]