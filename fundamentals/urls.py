from django.conf.urls import url
from fundamentals import views

urlpatterns = [
    url(r'^fundamentals_home/$', views.first, name="first"),
    url(r'^ytm/$', views.second, name="second"),
    url(r'^vob/$', views.fifth, name="fifth"),
    url(r'^vop/$', views.third, name="third"),
    url(r'^voe/$', views.fourth, name="fourth"),
]