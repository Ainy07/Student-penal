from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=200)
    
    
class Course(models.Model):
    coursename = models.CharField(max_length=200)
    coursefees=models.IntegerField()
    courseduration=models.CharField(max_length=100)
    coursetextbox=models.TextField()
    
    
def __str__(self):
        return self.course   
    
    
     
class AddStudents(models.Model):
    sname = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress= models.CharField(max_length=255)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourse= models.ForeignKey(Course , on_delete=models.CASCADE)     
    
def __str__(self):
        return self.sname   
    

GENDER_CHOICE = (
    {'M', 'Male'},
    {'F', 'Female'},
    {'O', 'Other'},
)
class Teacher(models.Model):
    teachername=models.CharField(max_length=300)
    employeesid = models.IntegerField()
    teacheremail=models.CharField(max_length=200)
    teacherpassword=models.CharField(max_length=300)
    teachermobile=models.IntegerField()
    joindate=models.DateField()
    education=models.CharField(max_length=100)
    workexp=models.CharField(max_length=200)
    photo = models.ImageField(upload_to='Teacher/')
    teachercourse=models.ForeignKey(Course , on_delete=models.CASCADE)  
    gender = models.CharField(choices=GENDER_CHOICE , max_length=200)
    is_active = models.BooleanField(default=True)