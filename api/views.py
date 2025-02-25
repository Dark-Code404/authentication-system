from auths.models import Todo
from .serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

"""
   A viewset for handling CRUD operations on Todo items.
    authentication_classes: A list of authentication classes used to authenticate the user.
    permission_classes: A list of permission classes used to restrict access to authenticated users.
    queryset: The set of Todo items to be used for list, retrieve, update, and delete actions.
"""


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
