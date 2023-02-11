# Retail_App

Steps to test Retail_api

1. First of all run the server using python manage.py runserver
2. Go to url http://127.0.0.1:8000/'api/accounts/register' and register by adding your credentials for example:
```
{
   "name" : "abc",
   "password": "124"
}
```
I use djangosimplejwt to authenticate user when you register as a user jwt generate a token using the hashing algorithm to authenticate the user.


3. Now go to url http://127.0.0.1:8000/api/v1/products to add products

4. Got to url http://127.0.0.1:8000/api/v1/cart to add the products into your cart as a user.

5. Go to url http://127.0.0.1:8000/api/v1/cartitems to add items to your cart the cart get updated when you add items and the total_price in cart gets updated.I add this functional uisng django signal but there is a minor bug in cartitems total prices not getting update.

6.Go to url http://127.0.0.1:8000/api/v1/orders to add order according to the cart(with total_price according to the quantity) with order id.
