from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rechargeapp.models import plan,customer,recharge_no
from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail
from datetime import datetime,time
from django.views import View


# Create your views here.
def home(request):
    p=plan.objects.all()
    context={'plans':p}
    return render(request,'prepaid.html',context)

def login_user(request):
    context={}
    if request.method=='POST':
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        if uemail=="" or upass=="":
            context['errmsg']="field cannot be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uemail,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['errmsg']="Invalid username and password"
                return render(request,'login.html',context)
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/home')

def register(request):
    context={}
    if request.method=='POST':
        uemail=request.POST['uemail']
        umob=request.POST['umob']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uemail=="" or umob=="" or upass=="" or ucpass=="":
            context['errmsg']="field cannot be empty"
            return render(request,'registration.html',context)
        elif upass!=ucpass:
            context['errmsg']="password and confirm password not same"
            return render(request,'registration.html',context)
        else:
            u=User.objects.create(username=uemail,email=uemail)
            u.set_password(upass)
            u.save()
            c=customer.objects.create(email=uemail,mobile=umob)
            c.save()
            context['success']="user created successfully"
            return render(request,'registration.html',context)
    else:
        return render(request,'registration.html')
    

def planfilter(request,dt):
    q1=Q(is_active=True)
    q2=Q(data=dt)
    p=plan.objects.filter(q1&q2)
    context={'plans':p}
    return render(request,'prepaid.html',context)
def sort(request,pr):
    if pr=='0':
        col='price'
    else:
        col='-price'
    p=plan.objects.filter(is_active=True).order_by(col)
    context={'plans':p}
    return render(request,'prepaid.html',context)

def sorts(request,pr):
    if pr=='0':
        col='price'
    else:
        col='-price'
    p=plan.objects.filter(data='-').order_by(col)
    context={'plans':p}
    return render(request,'postpaid.html',context)

def pdetails(request,pid):
    p=plan.objects.filter(id=pid)
    context={'plans':p}
    return render(request,'plan_details.html',context)

def payment(request,pid):
    p=plan.objects.filter(id=pid)
    for x in p:
        amt=x.price
        oid=random.randrange(1000,9999)
        client = razorpay.Client(auth=("rzp_test_oTkfAYQEfktFwW", "6Skss2O3zauBrlz0MxZKGlyX"))
        data = { "amount": amt*100, "currency": "INR", "receipt": str(oid) }
        payment = client.order.create(data=data)
        context={'data':payment,'pid':pid}
        return render(request,'payment.html',context)
    
def sendmail(request,Id):
    uemail=request.user.email
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    p=plan.objects.filter(id=Id)
    r=recharge_no.objects.all()
    for x in p:
        pr=x.price
        vd=x.validity
    for y in r:
        mob=y.rmobile
    send_mail(
        "Recharge succesfull",
        f"{date} \nRs.{pr} Recharge for {mob} through Razorpay has done successfully for {vd}",
        "ashishabak4@gmail.com",
        [uemail],
        fail_silently=False,)
    r.delete()
    return redirect('/home')
    
def prepaid(request):
    p=plan.objects.all()
    context={'plans':p}
    return render(request,'prepaid.html',context)

def postpaid(request):
    p=plan.objects.filter(data='-')
    context={'plans':p}
    return render(request,'postpaid.html',context)

def true5g(request):
    return render(request,'5g.html')

def locate(request):
    return render(request,'locate_us.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def mobile(request, pid):
    if request.method=='POST':
        rmob=request.POST['rmob']
        r=recharge_no.objects.create(rmobile=rmob)
        r.save()
        return redirect('/payment/{}'.format(pid))
    else:
        return render(request,'plan_details.html')

    