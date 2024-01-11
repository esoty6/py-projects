from polls.serializers.topping_serializer import ToppingSerializer
from polls.models import Pizza, Topping
from rest_framework import serializers


class PizzaSerializer(serializers.ModelSerializer):
  toppings = ToppingSerializer(many=True)
  
  class Meta:
    model = Pizza
    fields = ('id', 'name', 'toppings')