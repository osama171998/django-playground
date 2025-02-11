from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def aboutUs(request):
    templates = loader.get_template("about-us.html")
    return HttpResponse(templates.render())
