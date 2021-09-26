from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def order_view(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        print(post_data)
        message = "your order is pending"
        return JsonResponse({"msg":message})
    else:
        message = "request aborted"
        return JsonResponse({"msg":message})
