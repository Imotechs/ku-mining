from django.contrib import admin
from .models import Account,Profile,Mail,Withdrowal
# Register your models here.

admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Mail)
admin.site.register(Withdrowal)