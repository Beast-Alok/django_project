from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import*
# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone_number = request.POST.get('number')

        if(email == '' and username == ''and password == '' and name =='' and phone_number == ''):
            messages.info(request, 'Empty Fields are not allowed !')
            return redirect('/')
        else:
            allUser = Student.objects.filter(username = username).exists()
            if allUser:
                messages.info(request, 'This username is already registered !')
                return redirect('/')
            else:
                student = Student(email = email, username = username, password = password, name = name, phone_number = phone_number)
                student.save()
                messages.info(request, 'Student Registered Successfully !')
                return redirect('/login')
                
    return render(request, 'doctor/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(username == ''and password == ''):
            messages.info(request, 'Empty Fields are not allowed !')
            return redirect('/login')
        else:
            all_user = Student.objects.values('username','password')
            user_found = False
            for user_dict in all_user:
                if user_dict['username'] == username:
                    user_found = True
                    break
            if user_found:
                if user_dict['password'] == password:
                    messages.info(request, 'Logged In Successfully !')
                    return redirect('/appoint')
                else:
                    messages.info(request, 'Incorrect Password !')
                    return redirect('/login')
            else:
                messages.info(request, 'This username is not registered !')
                return redirect('/login')

    return render(request,'doctor/student_index.html')

def appoint(request):
    return render(request,'doctor/appoint.html')

def doctor_page(request):
    if request.method =='POST':
        issue = request.POST.get('issue')
        time = request.POST.get('time')
        location = request.POST.get('location')
        if(issue != None and time == None and location == None):
            doctor = Doctor.objects.filter(specialization = issue)

        elif(issue != None and time != None and location == None):
            doctor = Doctor.objects.filter(specialization = issue, time = time)

        elif(issue != None and time == None and location != None):
            doctor = Doctor.objects.filter(specialization = issue, location = location)

        else:
            doctor = Doctor.objects.filter(specialization = issue, time = time, location = location)

        if doctor != None:
            params = {'doctor':doctor}
            return render(request,'doctor/doctor.html',params)
        else:
            return redirect('/docPage')
        
    return render(request,'doctor/doctor.html')