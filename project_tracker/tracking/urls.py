from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:pk>/update/', views.update_project, name='update_project'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
]
