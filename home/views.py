from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from home.forms import StudentSearchForm
from home.forms import LoginForm
from home.models import Student
from home.forms import StudentEditModelForm
from home.forms import StudentCreateForm
from home.forms import UserRegistrationForm


# Create your views here.
def home_view(request):
    return render(request,'testpage.html')

def home_page(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')

def boot(request):
    return render(request,'boot.html')  

def homee(request):
    #del request.session['id']
    #request.session['id']='dell'
    if request.method=="POST":
        search=StudentSearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=Student.objects.filter(student_name__contains=value)
            return render(request,'homee.html',{'result':result,'form':StudentSearchForm()})
    else:
        form=StudentSearchForm()
        result=Student.objects.all()
        return render(request,'homee.html',{'form':form,'result':result}) 


def createstudent(request):
    if request.method=='POST':

        form=StudentCreateForm(request.POST)
        if form.is_valid():
            student=Student.objects.create(student_name=form.cleaned_data.get('student_name'),department=form.cleaned_data.get('department'))
            student.save()
            messages.success(request,'Created SUCEESSFULLY')
            return redirect('/homee')
    else:
        form=StudentCreateForm()
        return render(request,'create.html',{'form':form ,'value':'create'})



def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'Deleted Successfully!!',)
    return redirect('/homee')

def editstudent(request,id):
    request.session['id']=id
    student=Student.objects.get(id=id)
    if request.method=='POST':
        print("request.session['id']",request.session['id'])
        modelform=StudentEditModelForm(request.POST,instance=student)
        if modelform.is_valid():
            modelform.save()
            return redirect('/homee')

    else:
        modelform=StudentEditModelForm(instance=student)
        return render(request,'edit.html',{'form':modelform,'value':'Edit'})
        


def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserRegistrationForm()
    return render(request,'auth/signup.html',{'form':user_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'auth/login.html', {})

def user_logout(request):
        logout(request)
        return redirect('/')    

    #form=StudentSearchForm()
    #login=LoginForm()
    #msg='hello form from django'
    #context={'form':form,'msg':msg, 'login':login}
    #return render(request,'homee.html',context,)

