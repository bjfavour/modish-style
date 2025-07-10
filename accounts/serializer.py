from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get our custom user model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Password field won't be included in response
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    
    def create(self, validated_data):
        # Create and return a new user instance
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user