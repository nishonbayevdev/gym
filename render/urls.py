from django.urls import path
from .views import home
from .views import contact
from .views import sending
from .views import addPeople
urlpatterns=[
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('sending/',sending),
    path('add/',addPeople)
]
