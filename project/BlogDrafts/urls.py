from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('blogs/',views.Drafts,name='blogs'),
    path('create/',views.Create,name='create')
    
]