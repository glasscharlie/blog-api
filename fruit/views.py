from rest_framework import generics
from fruit.models import Fruit
from .serializers import FruitSerializer

class FruitList(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class FruitDetail(generics.RetrieveUpdateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
