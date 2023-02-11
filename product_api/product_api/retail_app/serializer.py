from rest_framework import serializers 
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'