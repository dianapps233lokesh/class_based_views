from django.shortcuts import render
from .models import GeeksModel
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

class createview(CreateView):
    model=GeeksModel
    fields=['title','description']
    template_name='/home/admin1/Desktop/django_tuts/class_based_views/class_based_views/templates/create.html'
    success_url='/'

class listview(ListView):
    model=GeeksModel
    template_name='/home/admin1/Desktop/django_tuts/class_based_views/class_based_views/templates/list.html'
    context_object_name='geeks_list'