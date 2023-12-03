from django.http import HttpResponse , JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render
# Create your views here.

#Para los html

def index(request):
    return render(request,'index.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return render(request,'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request,'projects.html')

def task(request):
    task = get_object_or_404(Task)
    return render(request,'task.html')
