from django.contrib import admin
from .models import Book,Categories,IssuedBook

model_list = [Book,Categories,IssuedBook]

admin.site.register(model_list)