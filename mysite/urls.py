"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('twitter.urls')),
    url(r'^', include('data.urls')),
    url(r'^', include('newsanalysis.urls')),
    url(r'^', include('googletrends.urls')),
    url(r'^', include('fundamentals.urls')),
    url(r'^', include('quants.urls')),
    url(r'^', include('calendar_events.urls')),
    url(r'^', include('forex.urls')),
    url(r'^', include('fii.urls')),
    url(r'^', include('commodity_markets.urls')),
    url(r'^', include('politics.urls')),
    url(r'^', include('industries.urls')),
    url(r'^', include('rating_agency.urls')),
    url(r'^', include('pair_trading.urls')),
    url(r'^', include('trading_algorithms.urls')),
]