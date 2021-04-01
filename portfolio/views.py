from django.shortcuts import render, get_object_or_404
from .models import Project, Blog


def home(request):
    projects = Project.objects.all()
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request, 'home.html', {'projects': projects, 'blogs': blogs})


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')  # [:3]
    return render(request, 'all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def index(request):
    blogs = Blog.objects.order_by('-date')[:3]
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects, 'blogs': blogs})
