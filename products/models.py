from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, serialize=False)
    product_category = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    productName = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    display_image = CloudinaryField('image')
    
    
    def __str__(self):
        return self.productName