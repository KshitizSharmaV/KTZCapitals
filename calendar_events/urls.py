from django.conf.urls import url, include
from calendar_events import views

urlpatterns = [
	url(r'^calendar_templates/$',views.first,name='first'),
]
