from django.http import HttpResponse
from django.shortcuts import render
from .models import Home

def home(request):
    homes = Home.objects.all()
    return render(request, 'home.html', {'homes': homes})
