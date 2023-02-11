from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200,null=False,blank=False)
    def __str__(self) -> str:
        return self.category_name

class Products(models.Model):
    product_image = models.ImageField(upload_to='retail_app/media', default='None.jpg')
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=5)
    selling_price = models.DecimalField(max_digits=7, decimal_places=5)
    quantity = models.IntegerField(max_length=200, default=0)

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=0)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user.username) + " " + str(self.product.name)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=200, blank=True)

@receiver(post_save, sender = CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_products = Products.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_products.selling_price)
    total_cart_items = CartItems.objects.filter(user = cart_items.user)
    cart = Cart.objects.get(id = cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()






    

