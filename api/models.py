from django.db import models
from django.contrib.auth.models import User
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

class Verfiy_user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    user_otp = models.SmallIntegerField()
    def __str__(self):
        return self.user.username





#single
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
import random

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        number = random.randint(1111,9999)
        subject = 'welcome to GFG world'
        message = f'Hi {instance.username}, thank you for registering in myblog \n Your OTP:{number}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        print(instance.email)
        send_mail( subject, message, email_from, recipient_list )
        Verfiy_user.objects.create(user=instance,user_otp=number)
