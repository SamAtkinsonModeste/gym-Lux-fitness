from django.views.generic import ListView
from .models import GymClasses

# Create your views here.


class GymClassesListView(ListView):
    model = GymClasses
    context_object_name = "gymclasses"
