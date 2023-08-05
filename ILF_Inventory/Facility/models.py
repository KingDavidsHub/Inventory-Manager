from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime

class FacilityItem(models.Model):
    name = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    tag = models.CharField(max_length=200, default='')
    owner = models.CharField(max_length=200, default='')
    date_purchased = models.DateField(default=datetime.date.today)
    warranty_period = models.IntegerField(default=10)
    warranty_expired = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='facility_items')

    def __str__(self):
        return self.name