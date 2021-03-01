from django.db import models

# Create your models here.

class Categories(models.Model):
    Categories_name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.Categories_name


class Item(models.Model):
    Item_categories = models.ForeignKey(Categories ,on_delete=models.CASCADE,related_name='item')
    Item_title = models.CharField(max_length=100)
    Item_Images = models.ImageField(upload_to='blog-images/')
    Item_Description = models.TextField()
    is_Active = models.BooleanField(default=False)
    is_Featured = models.BooleanField(default=False)
    def __str__(self):
        return self.Item_categories.Categories_name
