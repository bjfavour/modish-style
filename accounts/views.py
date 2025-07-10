from rest_framework import generics, status
from  rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserRegistrationSerializer



class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user =  serializer.save()
        return Response({
            "message": "User registered successfully",
            "user":serializer.data
        }, status=status.HTTP_201_CREATED)
        
        
        
class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Get the response from the original TokenObtainPairView
        response = super().post(request, *args, **kwargs)
        
        # Customize the response
        return Response({
            "access_token": response.data['access'],
            "refresh_token": response.data['refresh'],
            "message": "Login successful"
        }, status=status.HTTP_200_OK)

