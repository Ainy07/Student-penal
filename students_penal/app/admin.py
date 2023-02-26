from django.contrib import admin
from . models import *
# Register your models here.
@admin.register((Student))
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
    
    
@admin.register((Course))
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id','coursename','coursefees','courseduration','coursetextbox'] 
    

@admin.register((AddStudents))
class AddStudentsModelAdmin(admin.ModelAdmin):
    list_display=['sname', 'semail', 'smobile','saddress', 
                  'scollege', 'sdegree','scourse','total_amount',
                  'paid_amount','due_amount']      


@admin.register((Teacher))
class TeacherModelAdmin(admin.ModelAdmin):
    list_display=['teachername','employeesid', 'teacheremail', 'teachermobile','joindate', 
                  'education', 'workexp','photo','gender']      
    