from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Customerlogin, name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
