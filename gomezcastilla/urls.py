from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gomezcastilla.views.home', name='home'),
    # url(r'^gomezcastilla/', include('gomezcastilla.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','gomezcastilla.post.views.loop'),
	#url(r'^post/(?P<idpost>[0-9]+)/$','post.views.single'),
	url(r'^(?P<idpost>[-\w]+)/$', 'gomezcastilla.post.views.single', name='single'),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT},),
)
