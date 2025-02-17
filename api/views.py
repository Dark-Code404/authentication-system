from django.http import JsonResponse
from django.shortcuts import get_object_or_404 
from auths.models import Todo
from .serializers import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status
 
 

 
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def all_todo_data(request,pk=None):
    if request.method == "GET":
        id = pk
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
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
       return Response({"error": "User is not authenticated"}, status=401)


    if request.method =='PUT':

        if request.user.is_authenticated:
            

            id=pk
             

            if id is not None:
                todo=Todo.objects.get(id=id)
               
                serializer=TodoSerializer(todo,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)

                return Response(serializer.errors)
            return Response({"error": "id is none"}, status=401)
        return Response({"error": "User is not authenticated"}, status=401)
    

    if request.method =='PATCH':

        if request.user.is_authenticated:
            

            id=pk
            print(id)

            if id is not None:
                todo=Todo.objects.get(id=id)
               
                serializer=TodoSerializer(todo,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)

                return Response(serializer.errors)
            return Response({"error": "id is none"}, status=401)
        return Response({"error": "User is not authenticated"}, status=401)
    


    if request.method == "DELETE":

        if request.user.is_authenticated:
            

            id=pk

            if id is not None:
                todo=Todo.objects.get(id=id)
                todo.delete()
                return Response({"success":"Data deleted successfully"},)
               
                
            return Response({"error": "id is none"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "User is not authenticated"}, status=401)
        


     