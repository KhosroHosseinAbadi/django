from django import forms
from . models import School


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "principal": forms.Textarea(attrs={"class": "form-control"}),
            "location": forms.Textarea(attrs={"class": "form-control"}),
        }
