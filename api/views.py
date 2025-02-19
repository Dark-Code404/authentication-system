from auths.models import Todo
from .serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [AllowAny,]
    queryset = Todo.objects.all()
