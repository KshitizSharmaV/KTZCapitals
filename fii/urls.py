from django.conf.urls import url, include
from fii import views

urlpatterns = [
	url(r'^fii/$',views.first,name='first'),
	]
