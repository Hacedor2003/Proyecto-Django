from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

# Para los html


def index(request):
    title = 'Welcome to Django Course !!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = "Hacedor"
    return render(request, 'about.html', {
        "username": username
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        "projects": projects
    })


def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_proyect.html', {'form': CreateNewProject()})
    else:
        Project.objects.create(
            name=request.POST['name'])
        return redirect('projects')
