from django.conf.urls import patterns, include, url
#from appproyecto import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^appproyecto/', include('appproyecto.urls', namespace="appproyecto")),
	#url(r'^appproyecto/ingresar/$', views.ingresar, name='ingresar'),    
    url(r'^admin/', include(admin.site.urls)),
)


