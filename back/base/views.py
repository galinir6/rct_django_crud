from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET','POST','DELETE','PUT'])
def products(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_prod=Product.objects.get(id=id)
                return Response (ProductSerializer(temp_prod,many=False).data)
            except Product.DoesNotExist:
                return Response ("not found")
        all_prods=ProductSerializer(Product.objects.all(),many=True).data
        return Response ( all_prods)
    if req.method =='POST':
        prod_serializer = ProductSerializer(data=req.data)
        if prod_serializer.is_valid():
            prod_serializer.save()
            return Response ("post...")
        else:
            return Response (prod_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_prod=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")    
       
        temp_prod.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_prod=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")
       
        ser = ProductSerializer(data=req.data)
        old_prod = Product.objects.get(id=id)
        res = ser.update(old_prod, req.data)
        return Response('upd')
