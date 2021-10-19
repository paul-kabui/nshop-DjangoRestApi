from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from products.models import Product
from order.models import Order
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def order_view(request):
    if request.method == "POST":
        try:
            post_data = json.loads(request.body.decode("utf-8"))
            enteredMobileNumber = post_data['phoneNumber']
            enteredMpesaCode = post_data['mpesaCode']
            validNumber = '+254' + enteredMobileNumber
            myOrder = Order.objects.filter(mobileNumber = validNumber)
            if len(myOrder) != 0:
                for order in myOrder:   
                    mpesaCode = order.mpesaVerificationCode
                    if mpesaCode == enteredMpesaCode:
                        productNameList = order.productName.split(',')
                        userQuantity = order.quantityOrdered.split(',')
                        orderTotals = order.amountPaid
                        orderStatus = order.Status
                        orderList = []
                        if len(productNameList) == len(userQuantity):
                            for n in range(len(productNameList)):
                                finaldataformat = {
                                   'Name' : productNameList[n],
                                    'quantity' : userQuantity[n]
                                }
                                orderList.append(finaldataformat)  
                            myOrder = {
                                'orderedProducts' : orderList,
                                'orderStatus' : orderStatus,
                                'totals': orderTotals
                            }   
                            return JsonResponse({"info": myOrder})
                        else:
                            return JsonResponse({'info':'Error please contact us to follow on your order'})
                    else:
                        return JsonResponse({"info":"Invalid phone number or Mpesa code"})
            else:
                return JsonResponse({"info":"Invalid phone number or Mpesa code"})
        except:
            return JsonResponse({'info':'Error in your request,please contact us to follow on your order'})      
    else:
        return JsonResponse({"info":'Page not found'})