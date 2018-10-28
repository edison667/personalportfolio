from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(request):
    blogs = Blog.objects.all
    return render(request, 'blogs/allblogs.html', {'blogs':blogs})

def detail(request,blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blogdetail':blogdetail})
