from django.db import models

# Create your models here.

class Order(models.Model):
    productName = models.CharField(max_length=500)
    mobileNumber = models.CharField(max_length=15, null=False, blank=False)
    mpesaVerificationCode =models.CharField(max_length=50, blank=False)
    amountPaid = models.IntegerField(blank=False, null=False)
    quantityOrdered = models.CharField(max_length=500, blank=False, null=False)
    deliveryChoices = (('delivered','delivered'),('pendingDelivery','pendingDelivery'),('noDelivery','noDelivery'))
    deliveryStatus = models.CharField(max_length=20, choices=deliveryChoices,default='pendingDelivery')

    def __str__(self):
        return self.mobileNumber
