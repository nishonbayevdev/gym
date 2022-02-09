from django.shortcuts import render,redirect
from .models import Part ,Contact ,Subscribes,News

# Create your views here.
# homepage View
def home(request):
    part = Part.objects.all()
    news = News.objects.all()
    context = {
        'part1':part[0],
        'part2':part[1],
        'part3':part[2],
        'news':news
    }
    print(news[0].id)
    return render(request,'index.html',context)
# contact us view
def contact(request):
    return render(request,'contact.html')
# sending function
def sending(request):
    if request.method == 'POST':
        name     = request.POST['ism']
        phone = request.POST['tel']
        email    = request.POST['email']
        message  = request.POST['text']
        Contact(name=name,phoneNumber=phone,email=email,message=message).save()
    return redirect('/')
# add function over people
def addPeople(request):
    if request.method == 'POST':
        email = request.POST['qoshilish']
        listSubs = Subscribes.objects.all()
        flag = True
        for listSub in listSubs:
            if listSub.email == email:
                flag = False
        context = {
            'error' :False
        }
        if flag == True:
            Subscribes(email = email).save()
            return redirect('/')# must
        else:
            context['error'] = True
        return render(request,'index.html',context) #must
