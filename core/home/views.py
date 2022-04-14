from django.shortcuts import render
from requests import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentModelSerializer
from .models import Student

# Create your views here.

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentModelSerializer(student_objs, many=True)

    return Response({'status': 200, 'payload': serializer.data})

@api_view(['POST'])
def add_student(request):
    data = request.data
    serializer = StudentModelSerializer(data=data)

    if not serializer.is_valid():
        return Response({'message': 'bad request'})

    serializer.save()

    student_objs = Student.objects.all()
    serializer = StudentModelSerializer(student_objs, many=True)

    print(data)
    return Response({'payload': serializer.data})
