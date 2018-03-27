from django.conf.urls import url
from twitter import views

urlpatterns = [
    url(r'^twitterrunning/$', views.first, name="first"),
    url(r'^display_result/$', views.second, name="second"), # Add this /about/ route
]