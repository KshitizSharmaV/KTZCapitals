from django.conf.urls import url, include
from industries import views


urlpatterns = [
	url(r'^industries/$',views.industries,name='industries'),
	url(r'^sector_performance/$',views.sector_performance,name='sector_performance'),
	url(r'^sector_gdp/$',views.sector_gdp,name='sector_gdp'),
]
