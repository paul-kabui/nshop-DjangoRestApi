from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
import json
from django.core import serializers
from products.models import Product
from order.models import Order
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt 
def cart_view(request):
    if request.method == "POST":
        post_body = json.loads(request.body.decode("utf-8"))
        mobileNumber = post_body['telNumber']
        totalPrice = int(post_body['totalsPrice'])
        itemList = post_body['detailedItemList']
        priceList = []
        nameList = []
        quantityList = []
        validTotalPrice = 0
        for item in itemList:
            itemsId = int(item['id'])
            itemName = item['name']
            quantityOrdered = item['userQuanitity']
            validPrice = Product.objects.get(product_id=itemsId).price
            validCalcPrice = int(validPrice) * int(quantityOrdered)
            priceList.append(validCalcPrice)
            quantityList.append(quantityOrdered)
            nameList.append(itemName)
        for prices in priceList:
            validTotalPrice += prices
        if validTotalPrice == totalPrice:
            if len(mobileNumber) >= 10:
                int(mobileNumber)
                validMobileNumber = '+254' + mobileNumber
                names = str(nameList)
                orderedQuantity = str(quantityList)
                #intergrate mpesa api  from here
                order = Order(
                    productName = names,
                    mobileNumber = validMobileNumber,
                    mpesaVerificationCode = 'abcde',
                    amountPaid = validTotalPrice,
                    quantityOrdered = orderedQuantity,
                    deliveryStatus = 'noDelivery',
                )
                order.save()
                return JsonResponse({'msg': 'success'})
            else:
                return JsonResponse({'msg':'fail'}) 
            # 
            # 
            # )
           
        else:
            return JsonResponse({'msg':'fail'}) 
    else:
        return JsonResponse({'msg':'fail'})
