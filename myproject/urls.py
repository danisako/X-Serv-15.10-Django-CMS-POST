from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views
from django.contrib.auth.views import login,logout
from django.views.static import serve

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$','cms.views.index'),
	url(r'^login',login),
	url(r'^cms/(.+)$','cms.views.muestra'),
	url(r'^cms/(.+)/(.*)', 'cms.views.new_page'),
	url(r'^logout', logout),
	url(r'^accounts/profile', 'cms.views.redirect'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^edit/(.+)$', views.edit),
	url(r'static/(.*)$', serve, {'document_root': 'templates/plantilla'}),
)
