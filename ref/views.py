from django.shortcuts import render
from .models import case, tipsMod

# Create your views here.

def index(request):
    return render(request, 'ref/index.html', {'case': case.objects.all()})

def tip(request):
    return render(request, 'ref/tips.html', {'tips': tipsMod.objects.all()})

def prince(request):
    return render(request, 'ref/prince.html')

