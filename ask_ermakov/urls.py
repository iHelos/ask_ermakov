from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask_ermakov.views import *
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ask_ermakov.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       #    url(r'^', 'ask_ermakov.views.hello', name='hello'),
                       url(r'^$', index, name='index'),
                       url(r'^ask$', ask, name='ask'),
                       url(r'^signup$', register, name='register'),
                       url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                       url(r'^login$', 'django.contrib.auth.views.login',
                           {'template_name': 'user/login.html', 'redirect_field_name': '/question'}),
                       url(r'^settings$', profile, name='settings'),
                       url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='settings'), name='redirection'),
                       url(r'^question$', question),
                       )
