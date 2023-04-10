from . import views
from django.urls import path

urlpatterns = [
    path("<str:name>", views.greet, name="greet"),
    path("", views.index, name="index"),
]