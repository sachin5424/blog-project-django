from django.shortcuts import render
from  .models import Item,Categories
from .serializers import Item_serializer,Categories_serializer,Item_list_serializer
from rest_framework import generics
from rest_framework import permissions
# Create your views here.


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
    queryset = Item.objects.all()
    serializer_class = Item_serializer

class Blog_List(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = Item_list_serializer


class Blog_update_and_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = Item_serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
