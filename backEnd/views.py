from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

def home_view(request):
    context={}
    return HttpResponse('<h1>running !!</h1>')

@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({'Success': 'CSRF Cookie set'})

