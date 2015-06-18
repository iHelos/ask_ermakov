from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask_ermakov.views import index, ask, register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_ermakov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^', 'ask_ermakov.views.hello', name='hello'),
    url(r'^$', index, name='index'),
    url(r'^ask$', ask, name='ask'),
    url(r'^signup$', register, name='register'),
)
