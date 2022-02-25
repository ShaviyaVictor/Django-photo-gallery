from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request) :

  return HttpResponse('<h1>Memoir Home Page<h1>')



def gallery(request) :

  return HttpResponse('<h1>Gallery Page<h1>')


