from rest_framework import serializers
from auths.models import Todo


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
            'is_complete']
