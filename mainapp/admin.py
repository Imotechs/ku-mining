from django.contrib import admin
from .models import Trade,RandUser,UserPayEvidence,Deposit,Plan
# Register your models here.

admin.site.register(Trade)
admin.site.register(RandUser)
admin.site.register(UserPayEvidence)
admin.site.register(Deposit)
admin.site.register(Plan)