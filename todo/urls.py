from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('save_task/', views.save_task, name = 'save_task'),
    path('change_task_status/', views.change_task_status, name = 'change_task_status'),
    path('get/details/', views.get_details, name = 'get_details')
]
