from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def physics(request):
    return render(request, 'physics.html')
