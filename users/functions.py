import datetime
import random

def get_date():
    now = datetime.datetime.now()
    nday = datetime.timedelta(days = 1)
    due_time = now + nday
    print(due_time)
    return now, due_time


# def get_percentage(amount,percent):
#     percentage = percent/100
#     try:
#         interest = int(amount)*percentage
#         return interest
#     except Exception as er:
#         return None
def get_percentage(amount):
    if amount < 100:
        percentage = 0.05
        interest = int(amount)*percentage
        percent = 5
        return interest,percent
    elif amount >= 100 and amount<1000:
        percentage = 0.07
        interest = int(amount)*percentage
        percent = 7
        return interest,percent
    elif amount >= 1000 and amount< 5000:
            percentage = 0.10
            interest = int(amount)*percentage
            percent = 10
            return interest,percent
    elif amount >= 5000 and amount< 20000:
            percentage = 0.15
            interest = int(amount)*percentage
            percent = 15
            return interest,percent
    elif amount >= 20000:
        percentage = 0.25
        interest = int(amount)*percentage
        percent = 25
        return interest,percent

        
def make_new_deposit():
    now = datetime.datetime.now()
    time_str = ''.join(ch for ch in str(now) if ch.isalnum())
    num1 = time_str[3:8]
    print(num1)
    num2 = time_str[8:17]
    print(f'{num2}{num1}')
    return f'{num2}{num1}GT'


def get_game_time():
    now = datetime.datetime.now()
    nday = datetime.timedelta(minutes= 1)
    due_time = now + nday
    print(due_time)

    return due_time
    
def get_user_id():
    now = datetime.datetime.now()
    time_str = ''.join(ch for ch in str(now) if ch.isalnum())
    num1 = time_str[5:8]
    print(num1)
    num2 = time_str[8:15]
    print(f'{num2}{num1}')
    return f'{num2}{num1}'

def get_rand_user():
    num = [250,600,700,200,320,300,710,201,312,]
    return random.choice(num)

def get_referrer_percentage(amount):
    percentage = 0.4
    try:
        interest = int(amount)*percentage
        return interest
    except Exception as er:
        return er


