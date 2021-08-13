from django.db import models

# Create your models here.
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField,self).__init__(*args,**kwargs)
    def get_prep_value(self, value):
        return str(value).lower()


class Ingredient(models.Model):
    #name = models.CharField(max_length=30,unique=True)
    name = NameField(max_length=30,unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=30) #unit used e.g lbs oz
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}, {self.quantity}, {self.unit}, {self.unit_price}'

    def get_absolute_url(self):
        return '/ingredient/add'

class MenuItem(models.Model):
    #title = models.CharField(max_length=30,unique=True)
    title = NameField(max_length=30, unique=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.title}, {self.price}'

    def get_absolute_url(self):
        return '/'


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f'{self.menu_item}, {self.ingredient}, {self.quantity}'
    def get_absolute_url(self):
        return '/recipe/add'

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField() #this fields adds the hours and seconds.
    #timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.menu_item}, {self.timestamp}'

    def get_absolute_url(self):
        return '/'


