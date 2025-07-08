from django.shortcuts import render
from  rest_framework.response import Response
from  rest_framework import generics
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
        })

