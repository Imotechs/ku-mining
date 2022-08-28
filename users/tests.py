from django.test import TestCase

# Create your tests here.
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

print(get_percentage(20000))