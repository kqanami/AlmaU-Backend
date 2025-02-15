from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
