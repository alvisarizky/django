from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    
    title = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    
class Order(models.Model):
    items = models.TextField()
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.CharField(max_length=200)
    total = models.FloatField()
    