from django import forms
from todolist.models import Task
  
  
# creating a form
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"id": "title"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"id": "description"}))
    # create meta class
    class Meta:
        # specify model to be used
        model = Task
  
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]

