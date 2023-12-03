from django.http import HttpResponse , JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404
# Create your views here.

#Para los html

def index(request):
    return HttpResponse("Index Page")
def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)
def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)
def task(request,id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)
