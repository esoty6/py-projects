from django.db import models


class Topping(models.Model):
  class Meta:
    db_table = "toppings"
    
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name;
    
    
class Pizza(models.Model):
  class Meta:
    db_table = "pizzas"
    
  name = models.CharField(max_length=200)
  toppings = models.ManyToManyField(Topping, related_name="pizza")
  
  def __str__(self):
    return f'{self.name} - {", ".join(topping.name for topping in self.toppings.all())}';

class Restaurant(models.Model):
    class Meta:
      db_table = "restaurants"
      
    address = models.CharField(max_length=200)