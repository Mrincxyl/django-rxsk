from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Blog

# Create your views here.


def Drafts(request):
    return render(request,'allblogs.html')

@login_required(login_url='login')
def Create(request):
    
    categories = Category.objects.all()
    if request.method == 'POST':
        # handle add category
        if 'add_category' in request.POST:
            category = request.POST.get('category')
            
            if(category):
                Category.objects.get_or_create(name=category)
                messages.success(request,f'{category} Category Added Successfully.')
            else:
                messages.error(request,'Category Field is Required.')    
                return redirect('create')
                         
        # handle create blog
        if 'add_blog' in request.POST:
            pass    
            
        if  'delete_category' in request.POST:
            id = request.POST.get('delete_category') 
            dl_cat =  Category.objects.get(id=id)
            dl_cat.delete()
            messages.success(request,f"{dl_cat}  Deleted Successfully.")
            return redirect('create')
             
    return render(request,'create.html',{'data':categories})