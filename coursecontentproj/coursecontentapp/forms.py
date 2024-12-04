from django import forms
from .models import Course

class StudentForm(forms.Form):

    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField(
        help_text="Age should be Integer"
    )

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"


