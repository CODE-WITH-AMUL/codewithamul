from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')