from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def Login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'All fields are required')
            return redirect('login')
        
        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in Successfully')
            
            next = request.GET.get('next')
            if next:
                return redirect(next)   
            return redirect('home')
        
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
            
        
    return render(request,'login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('password')
        
        if not username or not email or not password:
            messages.error(request,"All fields are required")
            return redirect('register') 
        
        alreadyExist = User.objects.filter(username=username).exists()
        
        if alreadyExist:
            messages.error(request,'Username already exist')
            return render(request,'register.html')
        else:
            new_user = User.objects.create_user(username=username,password=password,email=email)
            new_user.save()
            messages.success(request,'User registered successfully🦋')
            return render(request,'login.html')
        
    return render(request,'register.html')

def Logout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('login')