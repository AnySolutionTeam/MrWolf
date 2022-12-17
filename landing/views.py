from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def facts(request):
    return render(request, "facts.html")

def feature(request):
    return render(request, "feature.html")

def project(request):
    return render(request, "project.html")

def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def terms(request):
    return render(request, "terms.html")

def testimonial(request):
    return render(request, "testimonial.html")
    
def error_404(request):
    return render(request, "error_404.html")
    
def support(request):
    return render(request, "support.html")

"""
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
"""