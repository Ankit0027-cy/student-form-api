from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from rest_framework import status
from.serializers import studentserializer
# Create your views here.
@api_view(['GET'])
def student_list(request):
    student=student.objects.all()
    serializer=studentserializer(student,many=True)
    return Response(serializer.data)


    
@api_view(['POST'])
def create_student(request):
    serializer=studentserializer(data=request.data)
    if serializer .is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_created)
    return Response(serializer.errors,status=status.Http_400_bad_request)
@api_view(['GET','PUT','PATCH','DELETE'])
def student_detail(request,pk):
    try:
        student=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=404)
    if request.method=='GET':
        serializer=studentserializer(student)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=studentserializer(student,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)   
    elif request.method=='PATCH':
        serializer=studentserializer(student,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
    elif request.method=='DELETE':
        student.delete()
        return Response(status=204)
