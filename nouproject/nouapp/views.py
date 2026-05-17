from django.shortcuts import render ,redirect ,reverse
from . models import Enquiry,Login,Student
from datetime import date
from adminapp .models import Program,Branch,Year,Notification,Coarses,Centers
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . import smssender
# Create your views here.
def index(request):
    noti=Notification.objects.all()
    return render(request,"index.html",{'noti':noti})


def aboutus(request):
    return render(request,"aboutus.html")
def gallery(request):
    return render(request,"gallery.html")
def registration(request):
    if request.method=="POST":
         
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        
        
        program=request.POST['program']
        branch=request.POST['branch']
        password=request.POST['password']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        usertype='Student'
        status='false'


        regdate=date.today()
        
        
        reg=Student(rollno=rollno ,name=name ,fname=fname ,mname=mname , gender=gender, address=address, program=program, branch=branch, year=year , contactno=contactno, emailaddress=emailaddress, regdate=regdate)
        reg.save()
        log=Login(userid=rollno, password=password,usertype=usertype, status=status)
        log.save()
        
        subject='Important Email from Nalanda Open University'
        msg=f'Hello {name} Your Registration is successfull. Your password is{password} for future login'
        email_from=settings.EMAIL_HOST_USER
        # send_mail(subject,msg,email_from,{emailaddress})
        messages.success(request,'Registration Completed')
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()

    noti=Notification.objects.all()
    return render(request,"registration.html",locals())
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
         obj=Login.objects.get(userid=userid ,password=password)
         if obj.usertype=="Student":
           request.session['rollno']=userid
           return redirect(reverse('studentapp:studenthome'))
           
         elif obj.usertype=="admin":
            request.session['adminid']=userid
            return redirect(reverse('adminapp:adminhome'))
            
        except :
            messages.success(request,'Invalid user')
    noti=Notification.objects.all()
    return render(request,"login.html",locals())
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        emailaddress=request.POST['emailaddress']
        number=request.POST['number']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        messages.success(request,'Enquiry is Submited')

       
        enq=Enquiry(name=name , gender=gender,address=address,number=number , enquirytext=enquirytext,enquirydate=enquirydate,emailaddress=emailaddress)
        enq.save()
        smssender.sendsms(number)
   
    return render(request,"contactus.html")
def news(request):
    return render(request,"news.html")
def acedimics(request):
    return render(request,"acedimics.html")
def coarses(request):

   
    crse=Coarses.objects.all()
    cntr=Centers.objects.all()
    return render(request,"coarse&center.html",locals())
def resume(request):
    return render(request,"resume.html")




