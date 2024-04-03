from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests,'app1/index.html')

def createstrategy(requests):
    return render(requests,'app1/createstrategy.html')

def margincalculator(requests):
    return render(requests,'app1/margincalculator.html')

def sinein(requests):
    return render(requests,'app1/login.html')