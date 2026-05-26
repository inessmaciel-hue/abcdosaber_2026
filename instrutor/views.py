from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def nome(request):
    return HttpResponse('<p>Minha View do App Instrutor</p>')