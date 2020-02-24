from .models import UserPost
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserPost
        fields = '__all__'