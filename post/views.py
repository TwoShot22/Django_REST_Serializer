# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer

# Status에 따라 직접 Response를 처리할 것
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# APIView를 상속받은 CBV
from rest_framework.views import APIView

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True) # QuerySet 넘기기 (many=True 인자)
        return Response(serializer.data) # 직접 Response Return 해주기 (serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): #직접 유효성 검사
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# PostList와 다르게, PK값을 받음
class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.object.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

