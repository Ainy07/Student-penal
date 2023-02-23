from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


# def update_student(request,uid):
#     if request.method == 'POST':
#         studentObj=Student()
#         uid = uid
#         studentObj.id=uid
#         studentObj.studentname = request.POST['name']
#         studentObj.studentemail = request.POST['email']
#         studentObj.studentmobile = request.POST['mobile']
#         studentObj.studentdegree= request.POST['degree']
#         id= request.POST['course']
#         studentObj.studentcourse=Course.objects.get(id=id)
#         studentObj.save()
#         student=Student.objects.all()
#         return render(request,'viewstudents.html',{'student':student})

# def updatestu(request,uid):
#     id=uid
#     res = Student.objects.get(id=id)
#     data=Course.objects.all()
#     return render(request, 'updatestudent.html', {
#         'stu':res,
#         'data':data
#     })


# def deletestudent(request):
#     sid=request.GET['sid']
#     Student.objects.get(id=sid).delete()
#     data=Student.objects.all()
#     return render(request,'viewstudents.html',{'data':data})            