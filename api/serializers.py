from rest_framework import serializers
from auths.models import Todo

"""
    Serializer for the Todo model that converts Todo instances to JSON format and vice versa.
    This serializer helps with serialization and deserialization of Todo datain API requests and responses.
"""


class TodoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Todo
        fields = [
            'id',
            'user',
            'name',
            'description',
            'date_posted',
            'updated_at',
            'complete_date',
            'is_complete',
        ]
