# # tasks/urls.py
# from django.urls import path
# from . import views
# from django.contrib.auth.views import LoginView, LogoutView

# urlpatterns = [
#     path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
#     path('', views.task_list, name='task_list'),
#     path('create/', views.task_create, name='task_create'),
#     path('edit/<int:pk>/', views.task_edit, name='task_edit'),
#     path('delete/<int:pk>/', views.task_delete, name='task_delete'),
# ]

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_tasks, name='view_all_tasks'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('filter/<str:priority>/', views.filter_tasks_by_priority, name='filter_tasks_by_priority'),
]
