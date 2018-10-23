from django.shortcuts import render, get_object_or_404
from .models import Blog
from jobs.models import Resume
# Create your views here.
def blog(request):
    blogposts = Blog.objects.all()
    resume = Resume.objects.filter(pk=1).first()
    return render(request, 'blog/blog_posts.html', {'blogposts': blogposts})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    resume = Resume.objects.filter(pk=1).first()
    return render(request, 'blog/detail.html', {'blog': blog})
