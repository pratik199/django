from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField('Student Name',max_length=30, null=True)
    dept= (
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    #photo=models.ImageField(upload_to='media/')
    department=models.CharField( 'Department',choices=dept,blank=True,null=True,max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name

class Book(models.Model):
    book=models.CharField('Book',max_length=100,null=True) 
    def __str__(self):
        return self.book   

class Teacher(models.Model):
    #teacher_id=models.CharField('Teacher ID' ,max_length=10,null=True)
    teacher_name=models.CharField('Teacher Name',max_length=30,null=True)  
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher_name
    
    #teacher_sal=models.CharField('Salary',max_length=30,null=True)

class Library(models.Model):
    library_name=models.CharField('Library',max_length=100,null=False)
    books=models.ManyToManyField('Book',null=True)
    def __str__(self):
        return self.library_name


 
   

class Parents(models.Model):
    #stu=models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
    father_name=models.CharField('Father Name',max_length=50)
    son=models.ManyToManyField('Student',null=True)
    def __str__(self):
        return self.father_name




class Section (models.Model):
    section=models.CharField('Section',max_length=20,null=False)
    advisor=models.OneToOneField('Teacher',on_delete=True,null=True)
    Student=models.ManyToManyField('Student',null=False)
    def __str__(self):
        return self.section

# class User(models.Model):
#     username=models.CharField('Username',max_length=20)
#     first_name=models.CharField('Firstname',max_length=50)
#     last_name=models.CharField('Lastname',max_length=50)
#     email=models.EmailField('Email',max_length=50)        

                

    