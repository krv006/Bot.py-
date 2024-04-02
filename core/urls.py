from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='categories-detail'),

    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

]