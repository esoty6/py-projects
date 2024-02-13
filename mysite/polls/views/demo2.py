from pprint import pprint
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from polls.serializers.topping_serializer import ToppingAndPizza, ToppingNameField, ToppingSerializer
from polls.serializers.pizza_serializer import PizzaSerializer

from polls.models import Pizza, Topping


class Demo2(APIView):
  def get(self, request: Request) -> Response:
    toppings = Topping.objects.prefetch_related('pizza')
    pizza_names = toppings.values('pizza__id','pizza__name', 'pizza__toppings')
    toppings = ToppingAndPizza(toppings, context={'pizza_names': pizza_names}, many=True).data
    
    pprint(toppings)
    
    return Response('ok', status=status.HTTP_200_OK)