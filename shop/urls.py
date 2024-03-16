from django.urls import path
from shop import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('product/<int:pk>/', views.ProductDetailAPIView.as_view()),

    path('cart/', views.CartCreateAPIView.as_view()),
    path('cart/<int:pk>/', views.CartUpdateDestroyAPIView.as_view()),
    path('cart/list/', views.CartProductsAPIView.as_view()),
]
