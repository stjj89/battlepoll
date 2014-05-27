from django.conf.urls import patterns, include, url
from battlepoll.views import admin_view, homepage_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', homepage_view),
    url(r'^admin/$', admin_view),
)

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'battlepoll.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )
