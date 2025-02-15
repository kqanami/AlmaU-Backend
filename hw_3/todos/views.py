from rest_framework import generics
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .serializers import TodoSerializer
from .forms import TodoForm

# API Views
class TodoListAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Web Views
class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"

class TodoDetailView(DetailView):
    model = Todo
    template_name = "todos/todo_detail.html"

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/todo_form.html"
    success_url = reverse_lazy("todo-list")

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todos/todo_confirm_delete.html"
    success_url = reverse_lazy("todo-list")
