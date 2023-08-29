from django.urls import path, include
from . import views

app_name = 'user_authentication'
# Defining url_patterns for user authentication
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.homepage, name='homepage'),
    path('authentication/<str:person>', views.authentication, name='authentication'),
    path('register/', views.RegisterForm.as_view(), name='register')

]
