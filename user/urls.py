from django.urls import path
from .views import usrlogin, logout, account, signup

urlpatterns = [
    path('', account, name="account"),
    path('login', usrlogin, name="account"),
    path('logout', logout, name="account"),
    path('signup', signup, name="account"),
]