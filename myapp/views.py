from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get(request):
  return HttpResponse("Hello Adrian, You're welcome.")

def post(request):
  return HttpResponse("You're in About")