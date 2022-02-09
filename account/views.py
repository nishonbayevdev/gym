from unicodedata import name
from django.shortcuts import render,redirect
from .models import CustumersSighnUp
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        obj : dict = {
            'fullname' : str(request.POST['fullname']),
            'userame'  : str(request.POST['userame']) ,
            'email'    : str(request.POST['email'])   ,
            'password' : str(request.POST['password'])
        }
        CustumersSighnUp(name=obj['fullname'],username=obj['userame'],emial=obj['email'],password=obj['password']).save()
    return render(request,'login.html')
def signin(request):
    if request.method == 'POST':
        for i in CustumersSighnUp.objects.all():
            if i.username == request.POST['username'] and i.password == request.POST['password']:
                return redirect(to='/')
    
    return render(request,'login.html') 