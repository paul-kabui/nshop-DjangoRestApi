from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt

@ensure_csrf_cookie
def Email_view(request):
    if request.method == "POST":
        email_body = json.loads(request.body.decode('utf-8'))
        print(email_body)
        return JsonResponse({'resp':'Email received'})