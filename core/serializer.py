from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'patronymic', 'position', 'salary',)


class DepartmentSerializer(serializers.ModelSerializer):
    employees = SerializerMethodField()

    class Meta:
        model = Department
        fields = ('name', 'employees',)

    def get_employees(self, obj):
        if 'view' not in self.context:
            raise AttributeError('View is a required argument for the context')

        view = self.context['view']
        queryset = Employee.objects.filter(department=obj)

        page = view.paginate_queryset(queryset)

        if page is not None:
            serializer = EmployeeSerializer(page, many=True)
            response = view.get_paginated_response(serializer.data)
            return response.data

        serializer = EmployeeSerializer(queryset, many=True)
        return serializer.data


def get_department_tree(parent_department=None, context=None):
    if context is None:
        context = {}

    departments = Department.objects.filter(parent_department=parent_department)
    department_dict = {}
    for department in departments:
        children_departments = get_department_tree(parent_department=department, context=context)
        department_data = DepartmentSerializer(instance=department, context=context).data

        department_dict[department.pk] = {
            **department_data,
            "children_departments": children_departments
        }
    return department_dict
