from django.urls import path

from . import views

urlpatterns = [
    path('departments/tree-view/', views.DepartmentTreeView.as_view(), name='department-tree-view'),
]
