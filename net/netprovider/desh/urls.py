from django.contrib import admin
from django.urls import path
from .views import *
from .models import *
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth import views as auth_view 

urlpatterns = [

	path('plans/',PlanData.as_view(),name='plans'),
	path('plansadd/',Planadd.as_view(),name='planadd'),
	path('plansdelete/<int:pk>',PlanDelete.as_view(),name='plandelete'),
	path('plansupdate/<int:pk>',PlanUpdate.as_view(),name='planupdate'),

   
    path("login/", auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("index/",Index.as_view(), name="index"),

    path('employee/',EmployeeData.as_view(),name='employee'),
	path('employeeadd/',Employeeadd.as_view(),name='employeeadd'),
	path('employeeupdate/<int:pk>',EmployeeDelete.as_view(),name='employeedelete'),
	path('employeedelete/<int:pk>',EmployeeUpdate.as_view(),name='employeeupdate'),

	path('custmor/',CustmorData.as_view(),name='custmor'),
	path('custmorview/',CustmorView.as_view(),name='custmorview'),
    
    path('complain/',Complainadd.as_view(),name='complain'),
    path('complainview/',ComplainView.as_view(),name='complainview'),
    path('complainupdate/<int:pk>',ComplainUpdate.as_view(),name='complainupdate'),
    path('complainupdatestatus/<int:pk>',ComplainUpdateStatus.as_view(),name='complainupdatestatus'),
    path('complaindelete/<int:pk>',ComplainDelete.as_view(),name='complaindelete'),
    
]
