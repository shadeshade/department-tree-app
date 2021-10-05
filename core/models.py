from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20)
    parent_department = models.ForeignKey(
        to='self', on_delete=models.SET_NULL, related_name='children_departments', null=True, blank=True
    )

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    department = models.ForeignKey(
        to=Department, on_delete=models.SET_NULL, related_name='employees', null=True
    )

    def __str__(self):
        return f'{self.name} {self.surname}'
