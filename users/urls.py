
from django.contrib import admin
from django.urls import path,include
from .views import (pending, register,
login,contact,profile,
deposit,WithdrawView,uploadEvidence,
transactions,settings,my_profile,game1,depositplans,
trade_success,cancel,approved,
EnterTrade,
)

urlpatterns = [
 path('accounts/sign_up/', register,name ='register'),
 path('accounts/sign_up/<str:ref>/', register),
 path('accounts/login/', login,name ='login'),
 path('contact/us/', contact,name ='contact'),
 path('profile/me/', profile,name ='profile'),
 path('profile/me/deposit/USDT/', deposit,name ='deposit'),
 path('profile/me/trade/all/', depositplans,name ='trade'),
 path('accounts/me/make/trade/<str:ref>/',EnterTrade.as_view(), name = 'make_trade'),
path('accounts/trade/success/',trade_success,name = "tradesuccess"),
 #withdraw url
 path('profile/me/withdraw', WithdrawView.as_view(),name = 'withdraw'),
 path('profile/me/uploads/', uploadEvidence, name = 'upload_evidence'),
 path('profile/me/transactions/',transactions, name = 'txns'),
 path('profile/me/history/pending/',pending, name = 'pending'),
 path('profile/me/history/cancel/',cancel, name = 'cancel'),
 path('profile/me/history/approved/',approved, name = 'approved'),
 path('profile/me/settings/',settings, name = 'settings'),
 path('profile/me/settings/me/',my_profile, name = 'my_profile'),
 #games
 path('games/number/guesing/',game1,name = 'game1'),
]
