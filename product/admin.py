from django.contrib import admin

from .models import Product, Category


admin.site.register(Category)
admin.site.register(Product)

# TODO: create categorys SMARTPHONES(Samsung, Iphone, Xiaomi),
#  Laptops(MacBook, ASUS, Acer), Eearphones
