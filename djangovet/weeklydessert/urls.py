from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)


urlpatterns =[
    path("", views.index, name="index"),
    #path('account/',include(("django.contrib.auth.urls",'weeklydessert'),namespace='weeklydesert')),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('signup/', views.SignUp.as_view(),name='signup'),
    path('logout/',views.logout_request,name='logout'),
    path('dessert/create',views.CreateDessertView.as_view(),name='createdessert'),
    path("polls/<int:pk>/", views.DetailsView.as_view(), name="detail"),
    path('polls/<int:week_id>/vote/',views.vote,name='vote'),
    path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results")
]