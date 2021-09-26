from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
import json
from django.core import serializers
from products.models import Product

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def cart_view(request):
    if request.method == "POST":
        try:
            post_body = json.loads(request.body.decode("utf-8"))
            tel_no = int(post_body['telNumber'])
            ids_list = post_body['ids']
            totals = int(post_body['totals'])

            product_prices = []
            for ids in ids_list:
                product_query = (Product.objects.get(pk=ids)).price
                product_prices.append(product_query)


            confirmed_totals = 0
            for prices in product_prices:
                confirmed_totals += prices
            if totals == confirmed_totals:
                message = "payment successful"
                return JsonResponse({'rensp':message})
            else:
                msg = 'payment failed'
                return JsonResponse({'resp':msg})
        except:
            return JsonResponse({'msg':"payment Aborted"})
    else:
        msg = 'request aborted'
        return JsonResponse({'resp':msg})