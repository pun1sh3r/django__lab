from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [

    path('',views.HomeView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('signup/', views.SignUp.as_view(),name='signup'),
path('home',views.HomeView.as_view(), name='home'),
    path('inventory/list', views.InventoryView.as_view(),name='inventory'),
    path('menu/list',views.MenuView.as_view(),name='menulist'),
    path('purchase/list',views.PurchaseView.as_view(),name='purchaselist'),
    path('ingredient/add/', views.IngredientAdd.as_view(),name='ingredientadd'),
path('ingredient/delete/<pk>', views.IngredientDelete.as_view(success_url="/inventory/list"),name='ingredientdelete'),
    path('ingredient/edit/<pk>', views.InventoryEdit.as_view(),name='ingredientedit',),
    path('menuitem/add/', views.MenuItemAdd.as_view(),name='menuitemadd'),
path('recipe/add/', views.RecipeAdd.as_view(),name='recipeadd'),
path('reports/', views.ReportView.as_view(),name='reports'),
path('order/add', views.OrderAdd.as_view(),name='orderadd'),

]