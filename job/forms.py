from django import forms
from .models import Job

class jobupload(forms.Modelform):
    class Meta:
        model = Job
        fields = "__all__"

