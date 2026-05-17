from django . urls import path
from . import views



urlpatterns= [
   path('adminhome/',views.adminhome,name="adminhome"),
   path('adminlogout/',views.adminlogout,name="adminlogout"),
   path('viewstudent/',views.viewstudent,name="viewstudent"),
   path('viewenquiry/',views.viewenquiry,name="viewenquiry"),
   path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
   path('viewcomplain/',views.viewcomplain,name="viewcomplain"),
   path('studymaterial/',views.studymaterial, name="studymaterial"),
   path('deletematerial/<ids>',views.deletematerial, name="deletematerial"),
   path('move/',views.move, name="move"),
   path('viewmaterials/',views.viewmaterials, name="viewmaterials"),
   path('newsevent/',views.newsevent, name="newsevent"),
   path('coarses/',views.coarses, name="coarses"),
   path('centers/',views.centers, name="centers"),
   path('deletecoarse/<id_s1>',views.deletecoarse, name="deletecoarse"),
   path('deletecenter/<id_s>',views.deletecenter, name="deletecenter"),
   path('viewcenter/',views.viewcenter, name="viewcenter"),
]


