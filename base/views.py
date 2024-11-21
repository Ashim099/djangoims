from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from.models import Product, Productcategory
from .serializers import ProductSerializer, ProductcategorySerializer
from rest_framework.response import Response
from rest_framework import status

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

    