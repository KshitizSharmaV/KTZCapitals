from django.conf.urls import url, include
from googletrends import views

urlpatterns = [
	url(r'^googletrends_display/$',views.first,name='first'),
	url(r'^googletrends/$',views.second,name='second'),
]