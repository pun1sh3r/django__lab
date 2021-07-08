from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list/', views.AttractionList.as_view(), name='statelist'),
    path('details/<statename>', views.details, name='details'),
    path('state/create', views.StateCreate.as_view(), name="statecreate"),
    path('state/delete/<pk>', views.StateDelete.as_view(success_url="/tourist_attractions/list"), name="statedelete"),
    path('state/update/<pk>', views.StateUpdate.as_view(success_url="/tourist_attractions/list"), name="stateupdate"),

    path('attraction/create', views.AttractionCreate.as_view(), name='attractioncreate'),
    path('attraction/delete/<pk>', views.AttractionDelete.as_view(success_url="/tourist_attractions/list"), name="attractiondelete"),
    path('attraction/update/<pk>', views.AttractionUpdate.as_view(success_url="/tourist_attractions/list"), name="attractionupdate"),

]