"""product_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product_api.retail_app import views


from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/v1/products', views.ProductViewSet, basename='product')
router.register('api/v1/categories', views.CategoryViewSet, basename='category')
router.register('api/v1/cart', views.CartViewSet, basename='cart')
router.register('api/v1/cartitems', views.CartItemsViewSet, basename='cartitems')
router.register('api/v1/orders', views.OrdersViewSet, basename='order')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/accounts/' , include('accounts.urls')),
    path('api/demo/' , views.DemoView.as_view()),
]
