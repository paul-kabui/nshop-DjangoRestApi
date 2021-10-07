from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from products.models import Product
from order.models import Order
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def order_view(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        enteredMobileNumber = post_data['phoneNumber']
        enteredMpesaCode = post_data['mpesaCode']
        validNumber = '+254' + enteredMobileNumber

        myOrder = Order.objects.filter(mobileNumber = validNumber)

        productList = []
        for order in myOrder:   
            code = order.mpesaVerificationCode
            if code == enteredMpesaCode:
                productName= ((order.productName).strip('[]')).split(',')
                print(productName)
        # orderItem = list(myOrder.productName)
        # orderQuantity = list(myOrder.quantityOrdered)
        # mobileNumber = myOrder.mobileNumber
        

        # print(validNumber, orderQuantity)

        return JsonResponse({"myOrder": 'dffdfd'})
    else:
        message = "request aborted"
        return JsonResponse({"msg":message})
