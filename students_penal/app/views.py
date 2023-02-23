from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http.response import HttpResponse
from . models import Student , Course , AddStudents , Teacher
# Create your views here.


def courses(request):
    data=Course.objects.all()
    return render(request,'courses.html',{"data":data})

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
    else:
        return render(request,'courses.html',{"data":data})
        
        
def update_view(request, uid):
    res = Course.objects.get(id=uid)
    return render(request, 'updatecourse.html', {'course': res,})  

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
    stu=AddStudents.objects.all()
    addcourses= Course.objects.all()
    redirect("/viewstudents/")
    return render(request, 'viewstudents.html', {'stu':stu, 'addcourses':addcourses})

def addstudent(request):
        if request.method == "POST":
            stu_name= request.POST.get("Name")
            stu_email= request.POST.get("Email")
            stu_mobile= request.POST.get("Mobile")
            stu_college= request.POST.get("College")
            stu_degree= request.POST.get("Degree")
            stu_address= request.POST.get("Address")
            stu_addcourse_id = request.POST.get("course")
            total_amount= request.POST.get("qty")
            paid_amount= request.POST.get("cost")
            due_amount= request.POST.get("DueAmount")
            stu_course= Course.objects.get(id=stu_addcourse_id)
            if AddStudents.objects.filter(semail=stu_email).exists():
                messages.error(request, "Email id already exists")
                return redirect("/addstudent/")
        
            elif AddStudents.objects.filter(smobile=stu_mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect("/addstudent/")
            else:
                AddStudents.objects.create( sname=stu_name, 
                                            semail=stu_email, 
                                            smobile=stu_mobile,
                                            scollege=stu_college,
                                            sdegree=stu_degree,
                                            saddress=stu_address,
                                            scourse=stu_course,
                                            total_amount=total_amount,
                                            paid_amount=paid_amount,
                                            due_amount=due_amount,
                                            )
                messages.success(request, "Student Added Successfully!!")
                stu=AddStudents.objects.all()
                addcourses= Course.objects.all()
                return render(request, 'viewstudents.html', {'stu':stu, 'addcourses':addcourses,
                                                                 })
        else:
            stu=AddStudents.objects.all()
            addcourses= Course.objects.all()
            return render(request, 'viewstudents.html', {'stu':stu, 'addcourses':addcourses})
        
        
        
def updatestu(request,uid):
    res = AddStudents.objects.get(id=uid)
    addcourses= Course.objects.all()
    
    return render(request, 'updatestudent.html', {'stu': res,'addcourses':addcourses})



def update_student(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        sname = request.POST['name']
        semail = request.POST['email']
        smobile= request.POST['mobile']
        sdegree=request.POST['degree']
        scourse = request.POST['course']
        AddStudents.objects.filter(id=uid).update(sname=sname, semail=semail,
                                           smobile=smobile,sdegree=sdegree,
                                           scourse=scourse
                                           )
        return redirect('/viewstudents/')
    
    
def delete(request,pk):
    use = AddStudents.objects.filter(id=pk).delete()
    return redirect("/viewstudents/")


def teacher(request):
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})


def addteacher(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Mobile=request.POST['mobile']
        Education=request.POST['education']
        Joindate=request.POST['joindate']
        Workexp=request.POST['workexp']
        Ctc=request.POST['ctc']
        if Teacher.objects.filter(teacheremail=Email).exists():
            messages.error(request,"ALREADY EXISTS")
            teacher=Teacher.objects.all()
            return render(request,'teacher.html',{'teacher':teacher})
        else:
            teacher=Teacher.objects.create(teachername=Name,teacheremail=Email,teachermobile=Mobile,education=Education,joindate=Joindate,workexp=Workexp,ctc=Ctc)
            teacher.save()
            messages.success(request,"Added Succesfully")
            teacher=Teacher.objects.all()
            return render(request,'teacher.html',{'teacher':teacher})
    return redirect('/teacher/')
      



def update_tech(request,uid ):
    res = Teacher.objects.get(id=uid)
    return render(request, 'update_tech.html', context={

        'teacher': res,
    })

def updateteacherdata(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        Name = request.POST['name']
        Email = request.POST['email']
        Mobile = request.POST['mobile']
        Education= request.POST['education']
        Joindate= request.POST['joindate']
        Work= request.POST['workexp']
        CTC= request.POST['ctc']
        Teacher.objects.filter(id=uid).update(teachername=Name,teacheremail=Email,
                                            teachermobile=Mobile,education=Education,
                                            joindate=Joindate,workexp=Work,ctc=CTC)
        return redirect('/teacher/')

def deleteteacher(request):
    tid=request.GET['tid']
    Teacher.objects.get(id=tid).delete()
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})


