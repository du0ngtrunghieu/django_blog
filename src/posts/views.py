from django.shortcuts import render
from .models import Post , Category

def index(request):
    qs= Post.objects.filter(featured = True)
    
    conten ={
        'data' : qs
    }
   
    return render(request , 'index.html', conten)

def blog(request):
    
    return render(request , 'blog.html', {})
def post(request):
    return render(request , 'post.html', {})