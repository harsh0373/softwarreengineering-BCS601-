from django . urls import path
from . import views



urlpatterns= [
   path('Studenthome/',views.studenthome,name="studenthome"),
   path('Sessionend/',views.studentlogout,name="studentlogout"),
   path('response/',views.response,name="response"),
   path('Discusionforum/',views.postquestion,name="postquestion"),
   path('postanswer/<qid>',views.postanswer,name="postanswer"),
   path('postans/',views.postans,name="postans"),
   path('viewanswer/<qid>',views.viewanswer,name="viewanswer"),
   path('changepass/',views.changepass,name="changepass"),
   path('studentprofile/',views.viewprofile,name="viewprofile"),
   path('viewmaterial/',views.viewmaterial,name="viewmaterial"),
]