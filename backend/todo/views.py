from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeesSerializer
from .models import Employees

# Create your views here.

class EmployeesView(viewsets.ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()

