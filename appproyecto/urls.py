from django.conf.urls import patterns, url

from appproyecto import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
     # ex: /appencuesta/5/
    #url(r'^$', views.ingresar, name='ingresar'),
	url(r'^ingresar$', views.ingresar, name='ingresar'),    
	url(r'^proyecto$', views.proyecto, name='proyecto'),    
	url(r'^nuevo_proyecto$', views.nuevo_proyecto, name='nuevo_proyecto'),    
	url(r'^mis_proyectos$', views.mis_proyectos, name='mis_proyectos'),    


    """url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /appencuesta/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /appencuesta/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    """
)