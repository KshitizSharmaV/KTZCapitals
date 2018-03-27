from django.conf.urls import url, include
from trading_algorithms import views


urlpatterns = [
	url(r'^mean_reversion_algorithm/$',views.mean_reversion_algorithm,name='mean_reversion_algorithm'),
	url(r'^market_neutral_strategy/$', views.market_neutral_strategy, name='market_neutral_strategy'),
	url(r'^black_scholes/$', views.black_scholes, name='black_scholes'),
]
