from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from product_api.retail_app.customAuth import CustomAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response 



class DemoView(APIView):
     permission_classes = [IsAuthenticated]
     def get(self ,request):
         return Response({'success' : "you are authenticated"})


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = Category.objects.all()
        return category

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product = Products.objects.all()
        return product


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.all()
        return cart

class CartItemsViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemsSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cartitem = CartItems.objects.all()
        return cartitem
class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order = Orders.objects.all()
        return order


def Report(self):
    total_sales = CartItems.quantity * float(Products.selling_price)
    total_cost = Products.cost
    total_profit = total_sales - total_cost
        



