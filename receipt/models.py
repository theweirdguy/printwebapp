from django.db import models

# Create your models here.
class Receipt(models.Model):
    photo_type = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    is_printed = models.BooleanField(default=False)