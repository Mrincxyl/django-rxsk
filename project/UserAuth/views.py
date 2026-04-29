from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import re
import random
from .models import OtpModel
from django.core.mail import send_mail
from django.conf import settings
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
        
        alreadyExist = User.objects.filter(email=email).exists()
        if alreadyExist:
            messages.error(request,'Email already exist')   
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

def ForgetPassword(request):
    
    if request.method == 'POST' and 'send_otp'  in request.POST:
        username_or_email = request.POST.get('username_or_email')
        if not username_or_email:
            messages.error(request,'Please Enter Your Username or Email.')
            return redirect('forget_password')
        else:
            user = None
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if '@' in username_or_email and re.match(email_regex, username_or_email):
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    messages.error(request,f"No user found with this email {username_or_email}")
                    return redirect('forget_password')
            else:
                try:
                    user = User.objects.get(username=username_or_email)
                except User.DoesNotExist:
                    messages.error(request, f"No user found with this username {username_or_email}")  
                    return redirect('forget_password')   
        otp = random.randint(1000,9999)
        new_otp = OtpModel(user=user,otp=otp)
        new_otp.save( )
        
        try:
            send_mail(
                    'Your OTP for Password Reset',
                    f'{otp}. It is valid for 10 minutes.',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,)
        except:
            messages.error(request, 'Failed to send OTP. Please try again.')
            return redirect('forget_password')
            
        messages.success(request,f'OTP sent to your email {user.email}')
        return render(request,'submit-otp.html',{'user':user})    
        
        
                   
    return render(request,'forget_password.html')
    
    #return render(request,'submit-otp.html')
    