"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import index_view, task_create_view, task_delete_view, task_view, task_update_view,task_delete_selected_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('task/add/', task_create_view, name = 'task_create'),
    path('task/delete/<int:pk>/', task_delete_view, name='task_delete'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('task/update/<int:pk>/', task_update_view, name ='task_update'),
    path('task/delete_selected/', task_delete_selected_view, name='task_delete_selected')
]
