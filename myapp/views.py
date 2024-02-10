from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'DJango Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'DavidAr55'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello " + username + "</h1>")

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })