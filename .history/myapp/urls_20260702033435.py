from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='list'),          # /students/
    path('create/', views.student_create, name='create'), # /students/create/
    path('<int:pk>/', views.student_detail, name='detail'), # /students/1/
    path('<int:pk>/update/', views.student_update, name='update'), # /students/1/update/
    path('<int:pk>/delete/', views.student_delete, name='delete'), # /students/1/delete/
]