from django.http import JsonResponse
from django.shortcuts import get_object_or_404 
from auths.models import Todo
from .serializers import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view 
 
 

 
@api_view(['GET','POST'])
def all_todo_data(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            todos=Todo.objects.get(id=id)
            serializer=TodoSerializer(todos)
            return Response(serializer.data)

        
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
         
    
    if request.method=="POST":
       if request.user.is_authenticated:
        

            post_data=request.data
            post_data['user']=request.user.id
            serializer=TodoSerializer(data=post_data)
            if serializer.is_valid():
                 
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
       return Response({"error": "User is not authenticated"}, status=401)
     