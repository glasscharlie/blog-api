from rest_framework import serializers
from fruit.models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = [
            'id', 'title', 'author','body', 'created_at'
        ]