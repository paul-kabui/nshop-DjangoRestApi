from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
from django.shortcuts import render

def csrf_view(request):
    rensponse = JsonResponse({'info':'sucess - set csrftoken'})
    rensponse['X-CSRFToken'] = get_token(request)
    return rensponse

# @ensure_csrf_cookie
@csrf_exempt
def Email_view(request):
    if request.method == "POST":
        email_body = json.loads(request.body.decode('utf-8'))
        # print(email_body)
        return JsonResponse({'info':'Email sent successfully'})
