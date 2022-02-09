from django.urls import path
from .views import register
from .views import register , login ,signup , signin
urlpatterns=[
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('register/signup/',signup,name='signup'),
    path('register/signin/',signin,name='signin')
]