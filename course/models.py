from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    phone = models.CharField(max_length=11 , null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    password = models.CharField(max_length=255)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    status = models.IntegerField(choices=[
        #(مقدار نمایش داده شده و مقدار ذخیره شده)
        (1, "در حال ثبت نام"),
        (2, "در حال برگزاری"),
        (3, "اتمام یافته"),
        (4, "لغو شده")
    ], default=1)
    is_deleted = models.BooleanField(default=False)


