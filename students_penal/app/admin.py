from django.contrib import admin
from . models import *
# Register your models here.
@admin.register((Student))
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']
    
    
@admin.register((Course))
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id','coursename','coursefees','courseduration','coursetextbox']    