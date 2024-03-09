from rest_framework import serializers

from .models import (
    Category,Kind,
    Person,
    Priority,Status,
    Subkind,
    Ticket
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'