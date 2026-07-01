from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def student_list(request):
    return HttpResponse("Welcome to the Students page!")
