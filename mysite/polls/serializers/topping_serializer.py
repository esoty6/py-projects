from polls.models import Topping
from rest_framework import serializers


class ToppingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topping
    fields = ('id', 'name',)
    
class ToppingNameField(serializers.ModelSerializer):
  # def to_representation(self, instance):
  #   return {'id':instance.id, 'name':instance.name}

  class Meta:
    model = Topping
    fields = ('id', 'name')
    
class ToppingAndPizza(serializers.ModelSerializer):
  pizza_name = serializers.SerializerMethodField()
  
  def get_pizza_name(self, obj):
    wtf = self.context['pizza_names'].filter(pizza__toppings=obj.id)
    # print(self.context['pizza__names'].filter(pizza__toppings__contains=obj.id))
    return wtf.name

  class Meta:
    model = Topping
    fields = ('__all__')