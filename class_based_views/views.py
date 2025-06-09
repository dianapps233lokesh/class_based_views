from django.shortcuts import render
from .models import GeeksModel
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import GeeksForm

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

class detailview(DetailView):
    model=GeeksModel
    template_name='/home/admin1/Desktop/django_tuts/class_based_views/class_based_views/templates/detail.html'


class updateview(UpdateView):
    model=GeeksModel
    template_name='/home/admin1/Desktop/django_tuts/class_based_views/class_based_views/templates/update.html'
    fields=[

        'title',
        'description'
    ]
    success_url='/'

class deleteview(DeleteView):
    model=GeeksModel
    template_name='/home/admin1/Desktop/django_tuts/class_based_views/class_based_views/templates/delete.html'
    success_url='/'

class formview(FormView):
    form_class=GeeksForm
    template_name='/home/admin1/Desktop/django_tuts/class_based_views/class_based_views/templates/forms.html'
    success_url='/'