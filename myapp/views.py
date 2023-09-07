from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, username):
  print(username)
  return HttpResponse("You're in Index")

def welcome(request):
  return HttpResponse("Hello Adrian, You're welcome.")

def about(request):
  return HttpResponse("You're in About")