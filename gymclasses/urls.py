from django.urls import path
from .views import GymClassesListView

urlpatterns = [
    path("", GymClassesListView.as_view(), name="home"),
]
