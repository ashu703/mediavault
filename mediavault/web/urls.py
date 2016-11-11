"""
URL patterns for 'web' app
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/?', views.login, name='explore'),
    url(r'^shared-items/?', views.shared_items, name='shared-items'),
]
