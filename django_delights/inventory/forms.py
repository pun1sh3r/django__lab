from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class IngredientEditForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
class IngredientAddForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
class MenuItemAddForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = "__all__"
class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"
class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
        widgets = {'timestamp' : DateTimePickerInput() }

    def clean(self):
        cleaned_data = super().clean()
        menuItem = cleaned_data.get('menu_item')
        recipe = RecipeRequirement.objects.filter(menu_item=menuItem)
        for r in recipe:
            if r.ingredient.quantity == 0:
                self.add_error("menu_item", "not enough {} supply to make recipe".format(r.ingredient.name))
                return
            quantity = (r.ingredient.quantity - r.quantity)
            r.ingredient.quantity = quantity
            r.ingredient.save()