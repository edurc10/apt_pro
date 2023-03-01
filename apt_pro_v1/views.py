from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import AptdealToday
from .serializers import TestDataSerializer
from django.http import HttpResponse
from apt_pro_v1 import serializers

# Create your views here.
# -------------------------------------------------------------------------------------------------
# real project start
# # -------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# def getTestDatas(request):
#     datas = AptdealToday.objects.all()
#     serializers = TestDataSerializer(datas, many=True)
#     return Response(serializers.data)

# @api_view(['GET'])
# def getTestData(request, price):
#     data = AptdealToday.objects.get(price=price)
#     serializers = TestDataSerializer(data, many=False)
#     return Response(serializers.data)

@api_view(['POST'])
def postMember(request):
    reqData = request.data
    serializer = TestDataSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def Aptdata(request, aptid):
    data = AptdealToday.objects.get(id = aptid)
    serializers = TestDataSerializer(data, many=False)
    return Response(serializers.data)

def main(request):
    return render(request, 'apt_pro_v1/main.html', {})

def apt2me(request):
    return render(request, 'apt_pro_v1/apt2me.html', {})