from django.conf.urls import url, include
from pair_trading import views


urlpatterns = [
	url(r'^pair_trading/$',views.pair_trading,name='pair_trading'),
]
