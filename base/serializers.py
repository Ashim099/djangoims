from rest_framework import serializers
from .models import Product, Productcategory,user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Productcategory
        fields = '__all__'

class Userserializer(serializers.Modelserializer):
    
    class Meta:
        model = user
        fields = ['username','password','email','image','address','contact']


