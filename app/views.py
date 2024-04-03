from django.shortcuts import render,redirect
from django.core.mail import send_mail  
import random

# Create your views here.

def home(requests):    
    return render(requests,'app1/index.html')

def createstrategy(requests):
    return render(requests,'app1/createstrategy.html')

def margincalculator(requests):
    return render(requests,'app1/margincalculator.html')

def sinein(requests):
    return render(requests,'app1/login.html')

def register(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Name = request.POST.get('fullname')
        Password = request.POST.get('password')
        Confirm_password = request.POST.get('confirm_password')

        if Password == Confirm_password:
            otp = random.randint(1000, 9999)

            request.session['otp']=otp
            data=render(request,'app1/login.html',{'otp':otp})
            # request.session['Name']="vaibhav"
            data.set_cookie('otp',otp)

             # Set session timeout to 2 minutes
            # request.session.set_expiry(120)

            subject = "Test_Mail for otp"
            message = f'Hello {Name},\n\nYour One Time Password (OTP) is: {otp}\n\nPlease use this OTP to verify your identity.\n\nThank you!'
            from_email = "vaibhvamalviya89@gmail.com"
            recipient_list = [Email]

            send_mail(subject, message, from_email, recipient_list)

            return data
        else:
            msg = "Password and Confirm Password is not Match"
            return render(request, 'app1/login.html', {'msg': msg})
    else:
        # Handle GET requests if needed
        msg="Request is not POST"
        return render(request, 'app1/login.html',{'msg':msg})

def otp_verify(request):
    V_otp=request.POST['opt']
    # session_otp=request.session['otp']
    session_otp = request.COOKIES['otp'] 
    
    V=int(V_otp)
    S=int(session_otp)
    # print(type(S),',',type(V))

    if V==S:
        return render(request,'app1/index.html')
    else:
        msg='OTP in not Verifed'
        return render(request, 'app1/login.html',{'msg':msg})
