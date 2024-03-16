from shop import models, serializers
from rest_framework import generics
from django.db.models import Count, Avg


class ProductListAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all().select_related('category')
    serializer_class = serializers.ProductListSerializer
    filterset_fields = ('category__title', 'brand__title')


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all().annotate(
        rating=Avg('ratings__star')
    )
    serializer_class = serializers.ProductDetailSerializer


class CartCreateAPIView(generics.CreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer


class CartUpdateDestroyAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer


class CartProductsAPIView(generics.ListAPIView):
    queryset = models.Cart.objects.all().select_related('product')
    serializer_class = serializers.CartListSerializer

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)

