from django import forms
from .models import Job

class jobform(forms.Modelform):
    class Meta:
        model = Job
        fields = "__all__"

