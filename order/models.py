from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model


class Address(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    is_paid = models.BooleanField(default=False)


class Order(BaseModel):
    class Status(models.TextChoices):
        DELIVERED = "DELIVERED"
        ONGOING = "ONGOING"
        CANCELLED = "CANCELLED"


    status = models.CharField(max_length=15, choices=Status.choices, default=Status.ONGOING)
