from django.http import HttpResponse , JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render
# Create your views here.

#Para los html

def index(request):
    title = 'Welcome to Django Course !!!'
    return render(request,'index.html', {
        'title':title
    })

def about(request):
    username = "Hacedor"
    return render(request,'about.html' , {
        "username":username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html' , {
        "projects":projects
    })

def task(request):
    tasks = Task.objects.all()
    return render(request,'task.html' , {
        'tasks':tasks
    })
