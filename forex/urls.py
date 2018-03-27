from django.conf.urls import url, include
from forex import views

urlpatterns = [
	url(r'^forex_template/$',views.first,name='first'),
	url(r'^currency_convertor/$',views.currency_convertor,name='currency_convertor'),
	url(r'^pip/$',views.pip,name='pip'),
	url(r'^margin/$',views.margin,name='margin'),
	url(r'^sandl/$',views.sandl,name='sandl'),
	]
