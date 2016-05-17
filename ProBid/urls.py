from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'untitled.views.home', name='home'),
    url(r'^$', 'user.views.login', name='userlogin'),
    url(r'^user$', include('user.urls')),
    url(r'^pro$', include('pro.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

