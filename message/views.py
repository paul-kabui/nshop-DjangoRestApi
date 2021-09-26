from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

# Create your views here
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def Email_view(request):
    if request.method == "POST":
        email_body = json.loads(request.body.decode('utf-8'))
        print(email_body)
        return JsonResponse({'resp':'Email received'})
