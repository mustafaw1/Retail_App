from django.contrib import admin
from .models import *


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Orders)
