from django.conf.urls import url
from newsanalysis import views

urlpatterns = [
    url(r'^newsdataanalysis/$', views.news_analysis_first, name="news_analysis_first"),
]