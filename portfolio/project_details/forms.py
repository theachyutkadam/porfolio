from django import forms
from .models import ProjectDetails
#DataFlair
class ProjectDetailsCreate(forms.ModelForm):
    class Meta:
        model = ProjectDetails
        fields = '__all__'
