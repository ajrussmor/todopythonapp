from django.forms import ModelForm
from .models import Todotab

class TodoForm(ModelForm):
    class Meta:
        model = Todotab
        fields = ['title','memo','important']
        
