from rest_framework import serializers
from ormapp.models import Employee,Company

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class CompanySerilizers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'