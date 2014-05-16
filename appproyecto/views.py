from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404
from django.template import RequestContext, loader
from appproyecto.models import Proyecto

# Create your views here.o
def index(request):
    return render_to_response('index.html')
        
def ingresar(request):
    return render_to_response('ingresar.html')

def proyecto(request):
    return render_to_response('proyecto.html')        

def nuevo_proyecto(request):
    return render_to_response('nuevo_proyecto.html')

"""def mis_proyectos(request):
    return render_to_response('mis_proyectos.html')
"""
 
def mis_proyectos(request):
    lista_proyectos=Proyecto.objects.all()
    context={'lista_proyectos':lista_proyectos}
    return render(request, 'mis_proyectos.html', context)

"""
    def detail(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, 'encuesta/detail.html', {'poll': poll})


    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
"""

"""def index(request):
    latest_poll_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'encuesta/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, 'encuesta/detail.html', {'poll': poll})
    """