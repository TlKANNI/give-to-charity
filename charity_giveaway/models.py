from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)


instituion_type = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna'),
)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=instituion_type, default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField(max_length=64)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField(max_length=9)
    city = models.CharField(max_length=128)
    zip_code = models.IntegerField(max_length=5)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pic_up_comment = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
