from rest_framework import serializers
from auths.models import Todo,CusUser
 

class TodoSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=Todo
        fields=['id','user','name','date_posted','complete_date','is_complete']
