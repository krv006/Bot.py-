from django.db import models
from django.db import models as m 
# Create your models here.

class Category(m.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Product(m.Model):
    name = models.CharField(max_length = 50)
    category = m.ForeignKey(Category, on_delete = models.CASCADE)