from django import forms
from .models import Job

class jobform(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
