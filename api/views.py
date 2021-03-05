from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view

from  .models import Blog,Categories,Verfiy_user
from .serializers import Item_serializer,Categories_serializer,Item_list_serializer,Users_serializer\
    ,User_list_serializer
from rest_framework import generics, status
from rest_framework import permissions
# Create your views here.


class Users_Create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Users_serializer

class Categories_Create(generics.CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = Categories_serializer

class Categories_List(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = Categories_serializer


class Categories_update_and_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = Categories_serializer



class Blog_Create(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Item_serializer

class Blog_List(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = Item_list_serializer


class Blog_update_and_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Item_serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def verfiy_user(request):

    if request.method == "POST":
        email = request.data.get("email")
        otp = request.data.get("otp")
        print(email)
        print(otp)
        if not email:
            return  Response({"email":"Email is requried"},status=status.HTTP_400_BAD_REQUEST)
        if not otp:
            return  Response({"otp":"email is requred"},status=status.HTTP_400_BAD_REQUEST)
        try:
            print(email)
            print(otp)
            user = User.objects.get(email=email)
            print(user,'user')
            if user.is_active == False:
                print(email)
        # print(otp)
                verfiy_users = Verfiy_user.objects.get(user=user)
                if verfiy_users.user_otp == otp:
                    user.is_active=True
                    user.save()
                    return Response({"successfully":"user created"},status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"email":"invalid Email"},status=status.HTTP_404_NOT_FOUND)

    return  Response({"request":"place valid details"},status=status.HTTP_400_BAD_REQUEST)


class User_List(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_list_serializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



# user


class Blog_details(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = Item_list_serializer
