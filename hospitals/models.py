import uuid
from django.db import models
from datetime import datetime
from django.urls import reverse

#from realtors.models import Realtor

class Hospital(models.Model):
  id = models.AutoField(primary_key=True, unique=True)
  hospital_name = models.CharField(max_length=200)
  rc_number = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  state = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  services = models.TextField(blank=True)
  equipment = models.TextField(blank=True)
  radiographers = models.CharField(max_length=200, blank=True)
  photo_main = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  photo_1 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
  reg_date = models.DateTimeField(default=datetime.now, blank=True)
  cac_certificate = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
  practice_license = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
  def __str__(self):
    return self.hospital_name

  def reg_date_pretty(self):
        return self.reg_date.strftime('%b %e %Y')

  def get_absolute_url(self):
	    return reverse("hospitals:update", kwargs={"id": self.id})






class Centre(models.Model):
  application_no = models.IntegerField(default=1000, blank=True)
  centre_name = models.CharField(max_length=200)
  rc_number = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  reg_date = models.DateTimeField(default=datetime.now, blank=True)
  cac_certificate = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
  practice_license = models.ImageField(upload_to='%Y/%m/%d/', blank=True)

  def __str__(self):
    return self.centre_name

  def reg_date_pretty(self):
        return self.reg_date.strftime('%b %e %Y')

  def get_absolute_url(self):
    return reverse("verify", kwargs={"id": self.id})
    return "/hospitals/%s/" %(self.id)

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
