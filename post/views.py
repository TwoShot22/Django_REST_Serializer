# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer

# Status에 따라 직접 Response를 처리할 것
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# APIView를 상속받은 CBV
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

     # Update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Destroy (Delete)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)