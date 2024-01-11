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