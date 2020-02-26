from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    # 어떤 Column을 기반으로 검색s할지 (Tuple)
    search_fields = ('title', 'body',)

    def get_queryset(self):
        qs = super().get_queryset()

        # .filter / .exclude
        #qs = qs.filter(author_id=1)

        # 로그인이 되어 있지 않다면
        if self.request.user.is_authenticated:
            # 지금 로그인한 User의 글만 Filtering
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)