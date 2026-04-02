from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100 ,unique=True)

    def __str__(self):
        return f'{self.name} Category'
    

class Blog(models.Model):
    visibility_option = [
        ('public','Public'),
        ('private', 'Private'),
    ]   
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True) 
    
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    
    visibility = models.CharField(max_length=10, choices=visibility_option,default='public')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} by {self.author.username}'
    