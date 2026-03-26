from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.



def Drafts(request):
    return render(request,'allblogs.html')

@login_required(login_url='login')
def Create(request):
    return render(request,'create.html')