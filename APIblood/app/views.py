from django.shortcuts import render,redirect
from rest_framework.response import Response
from .models import doner
from rest_framework import status
from .serializers import DonerSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def infosis(request):
    if request.method == 'GET':
        model = doner.objects.all()
        serializer = DonerSerializer(model, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=DonerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT','PATCH'])
def update_info(request, pk):
    info_obj = doner.objects.get(pk=pk)
    serializer = DonerSerializer(info_obj, data=request.data)
    #if serializer.is_valid():
        #serializer.save()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)
    

@api_view(['DELETE'])
def delete_info(request, pk):
    info_obj = doner.objects.get(pk=pk)
    info_obj.delete()
    model = doner.objects.all()
    serializer = DonerSerializer(model, many=True)
    return Response(serializer.data)