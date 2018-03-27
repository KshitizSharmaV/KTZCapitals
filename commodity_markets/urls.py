from django.conf.urls import url, include
from commodity_markets import views


urlpatterns = [
	url(r'^commodity_markets/$',views.first,name='first'),
	url(r'^mcx/$',views.mcx,name='mcx'),
	url(r'^ncdex/$',views.ncdex,name='ncdex'),
]
