from django.http import HttpResponse
from django.shortcuts import render

def predict(request):
    return render(request,'predict.html')

def homepage(request):
   return render(request,'homepage.html')

def base(request):
   return render(request,'base.html')
   

