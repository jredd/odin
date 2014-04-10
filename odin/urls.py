from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'odin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^asset-manager/', include('asset_manager.urls', namespace='asset_manager')),
    url(r'^admin/', include(admin.site.urls)),
)
