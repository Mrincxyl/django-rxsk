from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('blogs/',views.Blogs,name='blogs'),
    path('create/',views.Create,name='create'),
    path('blog/<slug:slug_value>/',views.BlogDetail,name='blog_detail')
    
]