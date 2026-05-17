from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from nouapp .models import Student,Enquiry,Login
from studentapp .models import StuResponse
from .models import Program,Branch,Year,Material,Notification,Coarses,Centers

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'adminhome.html',{'adminid':adminid})
    except KeyError:
        return redirect('nouapp:login')
def adminlogout(request):
    try: 
        del request.session['adminid']
        return redirect('nouapp:login')
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudent(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            student=Student.objects.all()
            return render(request,'viewstudent.html',locals())
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            enq=Enquiry.objects.all()
            return render(request,'viewenquiry.html',locals())
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedback(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            feed=StuResponse.objects.filter(responsetype='feedback')
            return render(request,'viewfeedback.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplain(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            complain=StuResponse.objects.filter(responsetype='complain')
            return render(request,'viewcomplain.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studymaterial(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            program=Program.objects.all()
            branch=Branch.objects.all()
            year=Year.objects.all()
            return render(request,'studymaterial.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def move(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            program=request.POST['program']
            branch=request.POST['branch']
            year=request.POST['year']
            subject=request.POST['subject']
            file_name=request.POST['filename']
            my_file=request.FILES['myfile']
            mt=Material(program=program,branch=branch,year=year,subject=subject,file_name=file_name,my_file=my_file)
            mt.save()
            return render(request,'studymaterial.html',{'adminid':adminid})
           
        
    except KeyError:
        return redirect('nouapp:login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewmaterials(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            mt=Material.objects.all()
            return render(request,'viewmaterials.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
def deletematerial(request,ids):
    
     mt=Material.objects.get(ids=ids)
     mt.delete()
     return redirect('adminapp:viewmaterials')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def newsevent(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=="POST":
               notification=request.POST['notification']
               noti=Notification(notification=notification)
               noti.save()
               noti=Notification.objects.all()
            return render(request,'newsevent.html',locals())
    except KeyError:
        return redirect('nouapp:login')
def deletenoti(request):
    
     return redirect('adminapp:newsevent')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def coarses(request):
    try:
        if request.session['adminid']!=None:
            if request.method=="POST":
               coarse=request.POST['coarse']
               crse=Coarses(coarse=coarse)
               crse.save()
        coarse=Coarses.objects.all()
        return render(request,'cntr&crses.html',{'coarse':coarse})
    except KeyError:
        return redirect('nouapp:login')
def centers(request):
    try:
        if request.session['adminid']!=None:
            if request.method=="POST":
               center=request.POST['center']
               cntr=Centers(center=center)
               cntr.save()

        return render(request,'cntr&crses.html',locals())
    except KeyError:
        return redirect('nouapp:login')
   
def deletecoarse(request,id_s1):
    
     crse=Coarses.objects.get(id_s1=id_s1)
     crse.delete()
     return redirect('adminapp:viewcenter')
def deletecenter(request,id_s):
    
     cntr=Centers.objects.get(id_s=id_s)
     cntr.delete()
     return redirect('adminapp:viewcenter')
def viewcenter(request):
    cntr=Centers.objects.all()
    coarse=Coarses.objects.all()
    return render(request,'coarses&center.html',locals())
