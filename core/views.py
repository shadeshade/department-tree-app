from django.views.generic import ListView

from .models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = 'core/index.html'
