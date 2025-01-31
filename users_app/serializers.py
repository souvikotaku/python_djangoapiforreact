from rest_framework import serializers
from .models import User  # Replace with your user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')