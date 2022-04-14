from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer

from .models import Student

class StudentModelSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'age']