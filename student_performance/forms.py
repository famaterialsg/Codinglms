from django import forms
from .models import StudentPerformance

# Form for creating and editing users
class StudentPerformanceForm(forms.ModelForm):
    class Meta:
        model = StudentPerformance
        fields = ['performance_id', 'user_id', 'course_id', 'quiz_id', 'assignment_id','score', 'feedback']

