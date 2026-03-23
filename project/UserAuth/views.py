from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Login(request):
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