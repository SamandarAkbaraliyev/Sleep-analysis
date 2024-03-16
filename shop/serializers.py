from rest_framework import serializers
from shop import models


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = models.Product
        fields = (
            'id',
            'title',
            'main_image',
            'category',
            'price',
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    rating = serializers.DecimalField(decimal_places=2, max_digits=3)

    class Meta:
        model = models.Product
        fields = (
            'id',
            'title',
            'description',
            'main_image',
            'category',
            'brand',
            'rating',
            'quantity',
        )


class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = models.Cart
        fields = (
            'product',
            'count',
            'user',
        )

    def create(self, validated_data):
        user = self.context.get('request').user
        instance = models.Cart.objects.create(user=user, **validated_data)
        return instance


class CartListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = models.Cart
        fields = (
            'id',
            'product',
            'count',
        )
