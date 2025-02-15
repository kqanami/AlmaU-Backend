from django.urls import path
from .views import TodoListAPI, TodoDetailAPI, TodoListView, TodoDetailView, TodoCreateView, TodoDeleteView


urlpatterns = [
    path('todos/', TodoListAPI.as_view(), name='todo-list-api'),
    path('todos/<int:pk>/', TodoDetailAPI.as_view(), name='todo-detail-api'),

    path('', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/new/', TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
]
