from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime

class ITItem(models.Model):
    staff_name = models.CharField(max_length=200, default='')
    devices = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=200, default='')
    floor = models.CharField(max_length=200, default='')
    technical_description = models.TextField(max_length=200, default='')
    computer_name = models.CharField(max_length=200, default='')
    ser_no = models.CharField(max_length=200, default='')
    win_version = models.IntegerField(default=10)
    supplier = models.CharField(max_length=200, default='')
    date_purchased = models.DateField(default=datetime.date.today)
    warranty_period = models.IntegerField(default=30)
    warranty_expired = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    comment = models.CharField(max_length=200, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='it_items')

    def __str__(self):
        return self.staff_name


# class Project(models.Model):
# 	name = models.CharField(max_length=200)

# 	class Meta:
# 		verbose_name_plural = 'project'

# 	def __str__(self):
# 		return self.name


class ITStore(models.Model):
    name = models.CharField(max_length=200, default='')
    total = models.IntegerField(default='')
    amount_assigned = models.IntegerField(default='')
    amount_left = models.IntegerField(default='')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='it_store')

    def __str__(self):
        return self.name