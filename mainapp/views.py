from django.shortcuts import render,redirect
import random
from django.contrib import messages
from users.models import  Mail
from .models import RandUser,Trade,Plan,Deposit
from django.utils import timezone
from users.models import Account
from users import functions
from django.db.models import Sum

from datetime import datetime,timedelta,date
from django.contrib.auth.models import User
# Create your views here.


def my_custom_error_view(request):
    return render(request,'error-500.html')

def page_not_found_view(request):
    return render(request,'error-404.html')
    
def page_restricted_view(request):
    return render(request,'error-403.html')
import os
import json
def home(request):
    # users = User.objects.all()
    # all = []
    # my_users = {}
    # for user in users:
    #     my_users.update({f'{user.username}':f'{user.email}'})
    #     all.append(my_users)

    # print(all)
    # with open('my_emails.txt','w') as f:
    #         f.write(str(all))

    trade = Trade.objects.filter(profited = False)
    time = timezone.now()
    for item in trade:
        if time >= item.due_time:
            item.profited = True
            #item.count += 1
            account,created = Account.objects.get_or_create(user = item.user)
            account.balance = account.balance + item.profit
            account.save()
            item.save()
            now,due = functions.get_date()
            if account.main > item.amount:
                interest,cent = functions.get_percentage(item.amount)
                new_trade = Trade.objects.create(
                    user =item.user,
                    amount = item.amount,
                    profit = interest,
                    time_now =now,
                    due_time = due,
                    count = item.count +1 
                )
                new_trade.save()

    if request.method =='POST':
        obj = Mail(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            subject = request.POST['subject'],
            message = request.POST['message'],   
            )
        obj.save()
        messages.success(request,'Mail Sent!')
        return redirect ('/')


        
    return render(request,'mainapp/index.html')


def news(request):
    return render(request,'mainapp/blog.html')

def terms(request):
    return render(request,'mainapp/terms.html')

def testimonial(request):
    return render(request,'mainapp/testimonial.html')
    
def about(request):
    return render(request,'mainapp/about-us.html')

