from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.db import models
from django.urls import reverse_lazy
from .models import *
from .forms import formulario1,formulario2
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


class postlista(ListView): 
     queryset=articulo_Cientifico.objects.filter(estado=1)
     template_name='articulos.html'

class ArticleDetailView(DetailView):
     model=articulo_Cientifico
     template_name='article_details.html'
     slug_field ='url'
     slug_url_kwarg = 'url'

   
class addArticulo(CreateView):
     model=articulo_Cientifico
     template_name='formulario.html'
     form_class=formulario1
     #fields='__all__'
     success_url=reverse_lazy('/articulos')



class addUsuario(CreateView):
      model=Usuario
      template_name='usuarios.html'
      form_class=formulario2
      success_url=reverse_lazy('/articulos')

def clima(request):
     return render(request,'clima.html')

def vistaTabla(request):
     return render(request,'vistaTabla.html',{'obj':articulo_Cientifico.objects.all()})


def home(request):
     return render(request,'home.html')
def inicial(request):
    
     return render(request,'index.html',{'ruta':'/static/css/main.css'})

def despedida(request):
     
     return render(request,'vista1.html')

