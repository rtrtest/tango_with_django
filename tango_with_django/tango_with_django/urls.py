from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls'))
)
    # Examples:
    # url(r'^$', 'tango_with_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


