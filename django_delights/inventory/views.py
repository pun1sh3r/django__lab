from django.shortcuts import render,redirect
from .models import MenuItem, RecipeRequirement, Ingredient,Purchase
from django.views.generic import ListView,DetailView,TemplateView, CreateView, UpdateView, DeleteView
from .forms import IngredientAddForm, OrderAddForm, MenuItemAddForm, RecipeAddForm, IngredientEditForm, UserForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import  LoginRequiredMixin
from collections import defaultdict
from django.urls import reverse_lazy

class SignUp(CreateView):
    success_url = reverse_lazy('login')
    form_class = UserForm
    template_name = 'registration/signup.html'


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'inventory/home.html'


    def get_context_data(self):
        context = super().get_context_data()
        context['ingredients'] = Ingredient.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['purchases'] = Purchase.objects.all()

        return context

class InventoryView(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"
class InventoryEdit(LoginRequiredMixin,UpdateView):
    model = Ingredient
    template_name = 'inventory/edit_inventory.html'
    form_class = IngredientEditForm
class MenuView(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = "inventory/menu.html"
    '''
    def get_context_data(self):
        context = super().get_context_data()
        menuItems = MenuItem.objects.all()
        menu_dict = defaultdict()
        context['menu_items'] = defaultdict()
        for item in menuItems:
            #menu_dict[item.title].update({'values' : set() })
            context['menu_items'].update({item.title: {'value' : set()}})
        for item in menuItems:
            recipes = RecipeRequirement.objects.filter(menu_item=item)
            for recipe in recipes:
                print(context)
                context['menu_items'][item.title]['value'].add(recipe.ingredient.name)

        return context
    '''
class PurchaseView(LoginRequiredMixin,ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
class IngredientAdd(LoginRequiredMixin,CreateView):
    model = Ingredient
    form_class = IngredientAddForm
    template_name = 'inventory/add_ingredient.html'
class IngredientDelete(LoginRequiredMixin,DeleteView):
    model = Ingredient
    template_name = 'inventory/delete_ingredient.html'
class MenuItemAdd(LoginRequiredMixin,CreateView):
    model = MenuItem
    form_class = MenuItemAddForm
    template_name = 'inventory/add_menuitem.html'
class RecipeAdd(LoginRequiredMixin,CreateView):
    model = RecipeRequirement
    form_class = RecipeAddForm
    template_name = 'inventory/add_recipe.html'
class OrderAdd(LoginRequiredMixin,CreateView):
    model = Purchase
    form_class = OrderAddForm
    template_name = 'inventory/add_order.html'
class ReportView(LoginRequiredMixin,TemplateView):
    template_name = 'inventory/reports.html'
    def calculate_cost(self):
        menu_items = MenuItem.objects.all()
        total_cost = 0
        for item in menu_items:
            recipes = RecipeRequirement.objects.filter(menu_item=item)
            total_cost += sum([r.quantity * r.ingredient.unit_price for r in recipes])
        return total_cost
    def get_context_data(self):
        context = super().get_context_data()
        orders = Purchase.objects.all()
        revenue = sum([ m.menu_item.price for m in orders])
        cost = self.calculate_cost()
        profit = '${:.2f}'.format(revenue - cost)
        context['total_revenue'] = "${:.2f}".format( revenue )
        context['profit'] = profit
        context['cost'] = '${:.2f}'.format(cost)

        return context
def logout_request(request):
    logout(request)
    return redirect("login")