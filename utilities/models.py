from django.db import models
from datetime import datetime
#from realtors.models import Realtor

class Hospital(models.Model):
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  state = models.CharField(max_length=200, blank=True)
  services = models.TextField(blank=True)
  equipment = models.TextField(blank=True)
  radiographers = models.CharField(max_length=200)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name

class License(models.Model):
  hospital_name = models.ForeignKey (Hospital, on_delete = models.CASCADE)
  license_id = models.CharField(max_length=100)
  license_category = models.CharField(max_length=100)
  issue_date = models.DateTimeField(default=datetime.now, blank=True)
  expiry_date = models.DateTimeField(default=datetime.now, blank=True)
  STATUS = (
     ('Active', 'Active'),
     ('Expired', 'Expired'),
    )
  status = models.CharField(max_length=10, choices = STATUS)
  def __str__(self):
    return self.license_id
