"""class_based_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  .views import createview,listview,detailview,updateview,deleteview,formview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',createview.as_view(),name='createview'),
    path('',listview.as_view(),name='geeks_list'),
    path('<int:pk>/',detailview.as_view()),
    path('<int:pk>/update',updateview.as_view()),
    path('<int:pk>/delete',deleteview.as_view()),
    path('forms',formview.as_view()),
]
