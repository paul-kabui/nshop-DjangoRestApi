from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home_view(request):
    context={}
    return HttpResponse('<h1>running !!</h1>')

