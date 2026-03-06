from django.shortcuts import render

def Home(request):
    return render(request,'home.html')

def Login(request):
    return render(request,'login.html')

def Register(request):
    return render(request,'register.html')