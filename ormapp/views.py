from django.shortcuts import render
from ormapp.models import Company,Employee
from rest_framework import generics
from ormapp.models import Employee
from ormapp.serializers import EmployeeSerilizer,CompanySerilizers

class EmployeeView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerilizer

class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerilizers


