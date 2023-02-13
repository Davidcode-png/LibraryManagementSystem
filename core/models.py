from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    isbn = models.PositiveIntegerField()
    category = models.ManyToManyField(Categories,related_name='categories')

    def __str__(self):
        return str(self.title) + " ["+str(self.isbn)+']'


def expiry():
    return datetime.today() + timedelta(days=14)
class IssuedBook(models.Model):
    student_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student') 
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='book')
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    fine = models.IntegerField(default=0,blank=True)