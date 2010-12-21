from django.conf.urls.defaults import *
from settings import ROOT, ADMIN_URL

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': ROOT+'/media'}),
    url(r'^'+ADMIN_URL+'/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('pages.urls')),
)
