from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from polls.serializers.topping_serializer import ToppingNameField, ToppingSerializer
from polls.serializers.pizza_serializer import PizzaSerializer

from polls.models import Pizza, Topping


class Demo(APIView):
  def get(self, request: Request) -> Response:
    pizza = PizzaSerializer(Pizza.objects.prefetch_related('toppings').get(id=1)).data
    toppingsId = [topping['id'] for topping in pizza['toppings']]
    toppings = ToppingSerializer(Topping.objects.filter(id__in=toppingsId), many=True).data
    
    # response =  list(map(lambda x: {**x, 'pizza': pizza['name']}, toppings))
    response =  [dict(item, pizza=pizza['name']) for item in toppings]
    
    return Response(response, status=status.HTTP_200_OK)