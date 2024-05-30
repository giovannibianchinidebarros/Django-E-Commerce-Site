from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    brand = models.CharField(max_length=200, default='Undefined')
    category = models.CharField(max_length=200, default='Undefined')
    description = models.TextField(default=0)
    thumbnail = models.CharField(
        max_length=300, default='https://tracerproducts.com/wp-content/uploads/2019/12/Product-Image-Coming-Soon.jpg')
    image = models.CharField(
        max_length=300, default='https://tracerproducts.com/wp-content/uploads/2019/12/Product-Image-Coming-Soon.jpg')

    def __str__(self):
        return self.title
