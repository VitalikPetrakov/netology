from django.http import HttpResponse as HR
from django.shortcuts import render

def home_view(request):
    return HR('Here will be a syte')