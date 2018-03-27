from django.conf.urls import url
from quants import views

urlpatterns=[
url(r'^quants_home/$', views.first, name="first"),
url(r'^table/$', views.second, name="second"),
]