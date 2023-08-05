from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BusinessItem(models.Model):
    staff_name = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200, default='-')
    quantity = models.IntegerField(default=0)
    floor = models.CharField(max_length=200, default='-')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='business_items')

    def __str__(self):
        return self.name
    

class BusinessStore(models.Model):
    name = models.CharField(max_length=200, default='')
    total = models.IntegerField(default='')
    assigned = models.IntegerField(default='')
    left = models.IntegerField(default='')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='business_store')

    def __str__(self):
        return self.name