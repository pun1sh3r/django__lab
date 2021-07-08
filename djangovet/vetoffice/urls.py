from django.contrib import admin
from django.urls import path, include
from . import views

# codec@demy123
urlpatterns = [
  path("", views.home, name="home"),
  #path('login/', views.login_view,name='login'),

    ]
'''

urlpatterns = [
   path('', views.home, name="home"),
   path('owner/list', views.OwnerList.as_view(), name="ownerlist"),
   path('owner/create', views.OwnerCreate.as_view(), name="ownercreate"),
  path("accounts/", include("django.contrib.auth.urls")),
  path("logout/", views.logout_view, name='logout'),
  path("signup/", views.SignUp.as_view(),name='signup'),
  path("owner/list", views.OwnerList.as_view(), name="ownerlist"),
  path("patient/list", views.PatientList.as_view(), name="patientlist"),
  path("owner/create", views.OwnerCreate.as_view(), name="ownercreate"),
  path("patient/create", views.PatientCreate.as_view(), name="patientcreate"),
  path("owner/update/<pk>", views. OwnerUpdateView.as_view(success_url="/owner/list"), name="ownerupdate"),
  path("patient/update/<pk>", views.PatientUpdate.as_view(success_url="/patient/list"), name="patientupdate"),
  path("owner/delete/<pk>", views.OwnerDelete.as_view(success_url="/owner/list"), name="ownerdelete"),
  path("patient/delete/<pk>", views.PatientDelete.as_view(success_url="/patient/list"), name="patientdelete"),
  path("appointment/list", views.AppointmentList.as_view(), name="apptlist"),
  path("appointment/create", views.AppointmentCreate.as_view(), name="apptcreate"),
  path("appointment/update/<pk>", views.AppointmentUpdate.as_view(), name="apptupdate"),
  path("appointment/delete/<pk>", views.AppointmentDelete.as_view(), name="apptdelete"),
]

'''