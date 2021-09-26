from django.shortcuts import render
from django.core import serializers
import json
from .models import Product
from django.http import HttpResponse, JsonResponse

# Create your views here.
def product_view(request):
    products = Product.objects.all()
    seralizedData = serializers.serialize("json", products)
    return JsonResponse({"products":seralizedData})
