from django.conf.urls import url, include
from politics import views

urlpatterns = [
	url(r'^politics/$',views.first,name='first'),
]