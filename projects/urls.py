from django.contrib import admin
from django.urls import path
from .views import project_list_view, project_detail_view


urlpatterns = [
    path('',project_list_view, name='project'),
    path('<int:pk>/',project_detail_view, name='project_detail')
    +
]