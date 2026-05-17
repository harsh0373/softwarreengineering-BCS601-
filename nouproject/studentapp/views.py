from django.shortcuts import render,redirect
from django .views.decorators.cache import cache_control
from nouapp . models import Student,Login
from . models import StuResponse,Question,Answer
from django.contrib import messages
from datetime import date
from adminapp .models import Material, Program


# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'studenthome.html', {'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
def studentlogout(request):
    try:
        del request.session['rollno']
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def response(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
              responsetype=request.POST['responsetype']
              subject=request.POST['subject']
              responsetext=request.POST['responsetext']
              responsedate=date.today()
              rollno=stu.rollno  
              name=stu.name
              branch=stu.branch
              year=stu.year
              program=stu.program
              contactno=stu.contactno
              emailaddress=stu.emailaddress
              sr=StuResponse(responsetype=responsetype,rollno=rollno,name=name,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,subject=subject,responsetext=responsetext,responsedate=responsedate,program=program)
              messages.success(request,'Response is Submited')

              sr.save()
            return render(request,'response.html', {'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postquestion(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                question=request.POST['question']
                postedby=stu.name
                posteddate=date.today()
                ques=Question(question=question,postedby=postedby,posteddate=posteddate)
                ques.save()
                messages.success(request,'Your Qustion has posted')
                
            ques=Question.objects.all()



            return render(request,'postquestion.html', {'stu':stu,'ques':ques})
    except KeyError:
        return redirect('nouapp:login')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ques=Question.objects.get(qid=qid)

            return render(request,'postanswer.html', {'stu':stu,'qid':qid,'ques':ques})
    except KeyError:
        return redirect('nouapp:login')


def postans(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=request.POST['qid']
            answer=request.POST['answer']
            answeredby=stu.name
            posteddate=date.today()
            ans=Answer(answer=answer,answeredby=answeredby,posteddate=posteddate,qid=qid)
            ans.save()
            messages.success(request,'Your Answer is posted')
            return redirect('studentapp:postquestion')   
    except KeyError:
        return redirect('nouapp:login')
def viewanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ans=Answer.objects.filter(qid=qid)

            return render(request,'viewanswer.html', {'stu':stu,'ans':ans})
    except KeyError:
        return redirect('nouapp:login')
    


def changepass(request):
    try:
        if request.session['rollno']!=None:
             rollno=request.session['rollno']
             stu=Student.objects.get(rollno=rollno)
             if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                cnewpassword=request.POST['cnewpassword']
                if newpassword!=cnewpassword:
                    messages.success(request,'new password and confirm password or not matched')
                    return render(request,"changepass.html",{'stu':stu})
                else:
                    try:
                     log=Login.objects.get(userid=rollno,password=oldpassword)
                     Login.objects.filter(userid=rollno).update(password=newpassword)
                     
                     return redirect('studentapp:studentlogout')
                    except :
                        messages.success(request,'Old Password is not matched')
             return render(request,"changepass.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'viewprofile.html', {'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmaterial(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            St=Student.objects.get(rollno=rollno)
            
            mt=Material.objects.filter(program=St.program ,branch=St.branch,year=St.year)
           
            return render(request,'viewmaterial.html', {'mt':mt})
    except KeyError:
        return redirect('nouapp:login')
    


   
