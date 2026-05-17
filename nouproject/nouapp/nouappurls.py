from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('registration',views.registration,name="registration"),
    path('login',views.login,name="login"),
    path('contactus',views.contactus,name="contactus"),
    path('news&updates',views.news,name="news"),
    path('acedimics/',views.acedimics,name="acedimics"),
    path('gallery/',views.gallery,name="gallery"),
    path('coarses/',views.coarses,name="coarses"),
    path('createresume/',views.resume,name="resume"),

]