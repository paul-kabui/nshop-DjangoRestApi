from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
import json
from django.core import serializers
from products.models import Product
from order.models import Order
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def cart_view(request):
    if request.method == "POST":
        try:
            post_body = json.loads(request.body.decode("utf-8"))
            mobileNumber = post_body['telNumber']
            totalPrice = int(post_body['totalsPrice'])
            itemList = post_body['detailedItemList']


            priceList = []
            productNameList = []
            userQuantityList = []

            # compare the total from frontEnd with this of backend
            # products ids and quantity ordered are the most crusial data
            validTotalPrice = 0
            for item in itemList:

                # get this from detailed list
                itemsId = int(item['id'])
                itemName = item['name']
                quantityOrdered = item['userQuanitity']

                # calculate the products total provided by db and user quantity
                validPrice = Product.objects.get(product_id=itemsId).price
                validCalcPrice = int(validPrice) * int(quantityOrdered)
                priceList.append(validCalcPrice)
                userQuantityList.append(str(quantityOrdered))
                productNameList.append(itemName)

            # calculating the whole cart total price
            for prices in priceList:
                validTotalPrice += prices

            #if the backendtotal price is equal to frontend total continue with the payments
            if validTotalPrice == totalPrice:
                if len(mobileNumber) >= 9 and len(mobileNumber) <= 10: #check the mobile number length
                    int(mobileNumber) # error if its not number
                    validMobileNumber = '+254' + mobileNumber #to be used by MpesaApi and to be stored in db

                    # make payment and process the data to be stored in db database
                    productNames = ','.join(productNameList)
                    orderedQuantity = ','.join(userQuantityList)

                    #intergrate mpesa api  from here
                    order = Order(
                        productName = productNames,
                        mobileNumber = validMobileNumber,
                        mpesaVerificationCode = 'abcde',
                        amountPaid = validTotalPrice,
                        quantityOrdered = orderedQuantity,
                    )
                    order.save()
                    return JsonResponse({'msg': 'success'})
                else:
                    return JsonResponse({'msg':'invalid phone number'}) 
            else:
                return JsonResponse({'msg':'Error in Totals! please try again'})
        except:
            return JsonResponse({'msg':'invalid phone number'}) 
    else:
        return JsonResponse({'msg':'Invalid request'})
