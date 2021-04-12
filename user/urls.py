from django.urls import path
from .views import login, logout, account, signup

urlpatterns = [
    path('', account, name="account"),
    path('login', login, name="account"),
    path('logout', logout, name="account"),
    path('signup', signup, name="account"),
]