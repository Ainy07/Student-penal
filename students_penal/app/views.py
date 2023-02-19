from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http.response import HttpResponse
from . models import Student , Course
# Create your views here.


def courses(request):
    return render(request,'courses.html')

def addcourse(request):
    if request.method=='POST':
        cr=request.POST['course']
        Duration=request.POST['duration']
        Fees=request.POST['fees']
        Comment=request.POST['comment']
        if Course.objects.filter(coursename=cr).exists():
            messages.error(request,"ALREADY EXISTS")
            data=Course.objects.all()
            return render(request,'courses.html',{"data":data})
        else:
            data=Course.objects.create(coursename=cr,courseduration=Duration,coursefees=Fees,coursetextbox=Comment)
            data.save()
            messages.success(request,"Added Succesfully")
            data=Course.objects.all()
            return render(request,'courses.html',{"data":data})
    return redirect('/courses/')

def updatecourse(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        course = request.POST['name']
        duration = request.POST['duration']
        fees = request.POST['fees']
        comment= request.POST['comment']
        Course.objects.filter(id=uid).update(coursename=course,courseduration=duration,coursefees=fees,coursetextbox=comment)
        return redirect('/courses/')


def delete(request):
    cid=request.GET['cid']
    Course.objects.get(id=cid).delete()
    data=Course.objects.all()
    return render(request,'courses.html',{'data':data})
 


def dashboard(request):
    return render(request,'dashboard.html')

def employees(request):
    return render(request,'employees.html')

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if Student.objects.filter(email=email).exists():
            obj = Student.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect("/dashboard/")
            else:
                return HttpResponse('password incorrect')
    else:
        return HttpResponse("email is not registered")



def notifications(request):
    return render(request,'notifications.html')

def pg_dashboard(request):
    return render(request,'pg_dashboard.html')

def profile(request):
    return render(request,'profile.html')

def signup(request):
    return render(request,'sign-up.html')

def formdata(request):
    if request.method == 'POST':
         name = request.POST['name']
         email = request.POST['email']
         password = make_password(request.POST['password'])
         if Student.objects.filter(email=email).exists():
             messages.error(request, "Email Already Exists")
             return redirect("/")
         else:
             Student.objects.create(name=name,email=email,password=password)
         return redirect("/login/") 

def tables(request):
    return render(request,'tables.html')

def tenants(request):
    return render(request,'tenants.html')

def viewstudents(request):
    return render(request,'viewstudents.html')

