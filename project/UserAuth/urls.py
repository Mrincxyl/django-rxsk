from django.contrib import admin
from django.urls import path
from UserAuth import views


urlpatterns = [
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register')
    
]