from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    uid = models.CharField(max_length=12, default= '',blank = True)
    country = models.CharField(max_length=30,null=True, default= '',blank = True)
    phone = models.CharField(max_length=30, null=True,default= '',blank = True)
    wallet_address =models.CharField(max_length=60,null=True, default= '',blank = True)
    wallet_type = models.CharField(max_length=60,null=True, default= '',blank = True)
    referrer = models.CharField(max_length=60, null=True, default= '',blank = True)
    referred = models.BooleanField(default= False)
    profited = models.BooleanField(default= False)

    def __str__(self):
        return f"{self.user}'s profile"


class Account(models.Model):
    user =  models.OneToOneField(User,on_delete= models.CASCADE)
    main = models.FloatField(blank=True, default= 0)
    balance =  models.FloatField(blank=True, default= 0)

    def __str__(self):
        return f"{self.user}'s"
        
class Mail(models.Model):
    name = models.CharField(max_length=30, blank = True)
    email = models.CharField(max_length=30,blank = True)
    phone=models.CharField(max_length=30,blank = True)
    subject = models.TextField(blank = True) 
    message = models.TextField(blank = True) 
    seen = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now=True)




class Withdrowal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0, verbose_name='USD')
    wallet_address = models.CharField(max_length=60, blank=True)
    date_placed = models.DateTimeField(blank=True,auto_now=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'