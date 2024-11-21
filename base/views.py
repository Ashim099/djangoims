from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from.models import Product, Productcategory
from .serializers import ProductSerializer, ProductcategorySerializer,Userserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  

class ProductcategoryApiView(GenericAPIView):
    queryset = Productcategory.objects.all()
    serializer_class = ProductSerializer

    def get(self,request):
        product_category_objs = self.get_queryset()
        serializer = self.get_serializer(product_category_objs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductcategoryDetailApiView(GenericAPIView):
    queryset = Productcategory.objects.all()
    serializer_class = ProductcategorySerializer

    def get(self,request,pk):
        product_category_objs = self.get_object()
        serializer = self.get_serializer(product_category_objs) 
        return Response(serializer.data)
    
    def put (self,request, pk):
        product_category_objs = self.get_object()
        serializer = self.get_serializer(product_category_objs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, pk):
        product_category_objs = self.get_object()
        product_category_objs.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    

#function based view
@api_view(['POST'])
def resister(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    data = request.data.copy()
    data['password'] = hash_password
    serializer = Userserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

    