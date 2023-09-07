from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
<<<<<<< HEAD

def index(request, username):
  print(username)
  return HttpResponse("You're in Index")

def welcome(request):
  return HttpResponse("Hello Adrian, You're welcome.")

def about(request):
  return HttpResponse("You're in About")

def porjects(request):
  projects = Project.objects.all();
  return JsonResponse(projects);

def tasks(request, title):
  # task = Task.objects.get(title= title)
  task = get_object_or_404(Task, title= title) # Funciona igual, pero sino lanzará un 404
  return HttpResponse('Task %s'%  task.title)
=======
def get(request):
  return HttpResponse("Hello Adrian, You're welcome.")

def post(request):
  return HttpResponse("You're in About")
>>>>>>> b2e4cb6adefb097403cd1dad9578ec17c56c7ef9
