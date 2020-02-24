from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer