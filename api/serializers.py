from rest_framework import serializers
from .models import Categories,Blog
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Users_serializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id', 'first_name','last_name','email','username','password']
    def create(self, validated_data):
        user = User()
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.username = validated_data['username']
        user.email = validated_data['email']
        user.password = make_password(validated_data['password'])
        user.is_active=False
        user.save()
        return user

    def validate(self, attrs):
        print(attrs)
        email = attrs['email']
        try:
            user = User.objects.get(email=email)
            if user:
                raise serializers.ValidationError({'email':"pls another email"})
        except User.DoesNotExist:
            return attrs
        # if not User.objects.get(email=email):
        # #     return attrs
        # user = User.objects.get(email=email)
        #
        # if user:
        #     raise serializers.ValidationError({'email':"pls another email"})
        # else:
        #     return attrs
        # return attrs


class User_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', 'first_name','last_name','email','username','password','is_active']


class Categories_serializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields=['id','Categories_name']
    def validate(self, attrs):
        if len(attrs['Categories_name'])<3:
            print(attrs)
            raise serializers.ValidationError({'title':'lenth 3'})
        return attrs


class Item_serializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','Blog_categories','Blog_title','Blog_Images','Blog_Description','is_Active','is_Featured']

class Item_list_serializer(serializers.ModelSerializer):
    Blog_categories = serializers.StringRelatedField()
    class Meta:
        model=Blog
        fields=['id','Blog_categories','Blog_title','Blog_Images','Blog_Description','is_Active','is_Featured']



class user_verfiy_serializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    opt = serializers.IntegerField(required=True)

