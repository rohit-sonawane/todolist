from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = TodoList
        fields = ('owner','id', 'date_created', 'description')
        read_only_fields = ('id',)