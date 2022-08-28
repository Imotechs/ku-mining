from django.urls import path
from django.views import View
from .views import (Dashboard, ActiveTrades,
SuccessfulTrades,AllUsers,AllDeposit,AllWithdraws,
MakeMail,Emails,ViewEmails,AdminUploadView

)
urlpatterns = [
    path('main/', Dashboard.as_view(), name='dashboard'),
    # path('staffs/', Staffs.as_view(), name = 'staffs'),   
    path('all/users/', AllUsers.as_view(), name = 'allusers'),
    path('current/deposits/', AllDeposit.as_view(), name = 'deposits'),
    path('current/withdrawals/', AllWithdraws.as_view(), name = 'withdraws'),
    path('all/mails/', Emails.as_view(), name = 'mails'),
    path('send/mails/', MakeMail.as_view(), name = 'sendmails'),
    path('view/<int:pk>/mails/', ViewEmails.as_view(), name = 'readmail'),
    path('view/active/trades/', ActiveTrades.as_view(), name = 'activetrades'),
    path('view/succesfull/trades/', SuccessfulTrades.as_view(), name = 'successfultrades'),
    path('uploads/views/', AdminUploadView.as_view(), name = 'evidenceview')
   
]
