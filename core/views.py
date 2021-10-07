from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializer import get_department_tree


class DepartmentTreeView(GenericAPIView):
    paginator = PageNumberPagination()

    def get(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        data = get_department_tree(context=context)
        return Response(data)
