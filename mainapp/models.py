from django.db import models
from django.contrib.auth.models import User

from users import functions

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=50,null = True)
    min = models.PositiveIntegerField(default=0)
    percentage_return = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    # plan = models.ForeignKey(Plan, null = True,on_delete=models.SET_NULL)
    # option = models.CharField(max_length=15, blank=True)
    date = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user}'

class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0,verbose_name=('USDT'))
    profit = models.FloatField(default=0)
    count = models.PositiveIntegerField(default=1)
    #deposit =  models.ForeignKey(Deposit,null = True,on_delete=models.SET_NULL)
    time_now = models.DateTimeField()
    due_time = models.DateTimeField()
    profited = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user}'

    @property
    def get_percent(self,*args,**kwargs):
        prof,cent = functions.get_percentage(self.amount)
        return cent


class RandUser(models.Model):
    count = models.IntegerField(default=3)
    views = models.IntegerField(default=5,null=True, blank=True)

class UserPayEvidence(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    evidence = models.ImageField(verbose_name = 'A photo of your payment Evidence',upload_to = 'media/payment_Evidence')
    date_upload = models.DateTimeField(auto_now=True)
    def get_total_evidence(self):
        return self.objects.all().count()
  
