from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mitao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'mitaoapp.views.register'),
    url(r'^edit/$', 'mitaoapp.views.traveledit'),
    url(r'^list/$', 'mitaoapp.views.travellist'),
    #url(r'^view/1/$', 'mitaoapp.views.traveldetail'),
    url(r'^detail/(?P<detail_id>\d+)/$', 'mitaoapp.views.traveldetail', name='traveldetail'),

    url(r'^admin/', include(admin.site.urls)),
)
