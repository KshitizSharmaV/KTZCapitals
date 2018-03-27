from django.conf.urls import url, include
from rating_agency import views


urlpatterns = [
	url(r'^rating_agency/$',views.rate,name='rate'),
	url(r'^rating_agency/(?P<id>[\w\-]+)/$', views.detail, name='detail'),
]
