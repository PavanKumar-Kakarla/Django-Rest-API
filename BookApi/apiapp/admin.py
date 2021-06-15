from django.contrib import admin
from .models import Book,Customer_Order

# Register your models here.

admin.site.register(Book)
admin.site.register(Customer_Order)