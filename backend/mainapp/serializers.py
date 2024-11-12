from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    preview = serializers.ImageField()
    director = serializers.CharField()


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')



class UserRegistrationsSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password1', 'password2')
        extra_kwargs = {'password': {"write_only": True}}

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        
        return attrs
    

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        return CustomUser.objects.create_user(password=password, **validated_data)
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        user = authenticate(**data)

        if user and user.is_active:
            return user
        
        raise serializers.ValidationError('Неверный email или пароль')