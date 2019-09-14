from django.shortcuts import render
from django.core.mail import send_mail
from math import ceil
from .models import *
def Home(request):
    top=Topper.objects.all()
    birthday=Birthday.objects.all()
    pics=MainPics.objects.all()
    news=News.objects.all()
    notice=Notice.objects.all()
    return render(request,"index.html",{"Top":top,"Birth":birthday,"Pic":pics,"News":news,"notice":notice})

def NewsPage(request,num):
    news=News.objects.get(id=num)
    return render(request,"news.html",{"News":news})


def Images(request):
    Picks = MainPics.objects.all()
    return render(request,"image2.html",{"Picks":Picks,"num":len(Picks)})
def Mission(request):
    return render(request,"mission.html")

def Rules(request):
    return render(request,"rules.html")

def Admision(request):
    return render(request,"admision.html")

def Features(request):
    return render(request,"features.html")

def About(request):
    return render(request,"about.html")

def Principle(request):
    return render(request,"principle.html")

def Sports(request):
    return render(request,"Sports.html")

def Contactus(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        send_mail(subject,msg,email,["vishankchauhan1@gmail.com",])

    return render(request,"contact.html")

def videoGalary(request):
    d=VideoGalary.objects.all()
    data=d[0].videofile
    return render(request,"video.html",{"vid":data})