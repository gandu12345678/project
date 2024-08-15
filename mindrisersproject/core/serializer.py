from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from random import randint
User=get_user_model()




class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30,)
    password = serializers.CharField(max_length=30,write_only=True)
    confirm_password=serializers.CharField(max_length=30,write_only=True)
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('emai already exists')
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'confirm_password':'passwords doesnot match',
            })
        return super().validate(attrs)
    
    def create(self, validated_data,*args,**kwargs):
        
        
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data['password'],
            )
        user.otp=randint(00000,99999)
        user.save()
        subject = 'activate your account'
        message = f'''
        Hi {user.username}, thank you for registering in Hamro inventory management system.
        Your otp for activating your accoutn is {user.otp}
        '''
        email_from = 'hims@gmail.com'
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return 
    
class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    
class UserActivationSerialzier(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.IntegerField()