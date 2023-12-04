from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('projects/',views.projects),
    path('task/',views.task),
    path('create_task/',views.create_task),
]
