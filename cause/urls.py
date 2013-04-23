from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('cause.views',
    url("^$", "home", name="home"),
    url(r'^(?P<pageslug>[\w-]+)/$', 'cause'),
)
