from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests,'app1/bash.html')
