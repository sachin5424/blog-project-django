from rest_framework import serializers
from .models import Categories,Item

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
        model=Item
        fields=['id','Item_categories','Item_title','Item_Images','Item_Description','is_Active','is_Featured']


class Item_list_serializer(serializers.ModelSerializer):
    Item_categories = serializers.StringRelatedField()
    class Meta:
        model=Item
        fields=['id','Item_categories','Item_title','Item_Images','Item_Description','is_Active','is_Featured']
