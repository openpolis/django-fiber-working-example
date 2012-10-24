from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'', 'fiber.views.page'),
)
