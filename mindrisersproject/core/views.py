from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from .serializer import UserRegisterSerializer,UserLoginSerializer,UserActivationSerialzier
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from django.contrib.auth import get_user_model,authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

User = get_user_model()
class UserViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer
    
    @swagger_auto_schema(
        methods=["POST"],
        request_body=UserLoginSerializer
        )
    
    @action(detail=False,methods=['POST'])
    def login(self,request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            )
        if user:
           token,_= Token.objects.get_or_create(user=user)
           return Response({
               "user":serializer.data,
               "token":token.key,
               })
        return Response(
            {"detail":"Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
            )
        
    @swagger_auto_schema(
        methods=['POST'],
        request_body=UserActivationSerialzier,
    )
    @action(detail=False,methods=['POST'])
    def activation(self,request):
        serializer=UserActivationSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user=User.objects.get(
                email=serializer.validated_data['email'],
                otp=serializer.validated_data['otp'],
            )
            user.is_active=True
            user.save()
            return Response({
                "details":"your account has been successfully activated"
            })
        except User.DoesNotExist:
            return Response(
                {'details':"email or otp doesont match"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        