from django.shortcuts import render

def index(request):
    return render(request,'TaskLoad/index.html')
