from rest_framework.viewsets import ModelViewSet
from base.models import Employee, Department
from base.serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
