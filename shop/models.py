from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Brand(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='products/')
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Image(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')


class Rating(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    star = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0)


class Cart(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'product')

