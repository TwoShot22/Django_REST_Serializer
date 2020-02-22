from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('post/',views.PostList.as_view()),
    # 127.0.0.1:8000/post/<pk> == DetailView
    path('post/<int:pk>/',views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)