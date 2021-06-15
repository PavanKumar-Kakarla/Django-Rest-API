from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            return user
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password')
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name','author')