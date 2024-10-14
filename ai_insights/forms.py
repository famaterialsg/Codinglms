from django import forms
from .models import AI_Insights

# Form for creating and editing users
class AI_InsightsForm(forms.ModelForm):
    class Meta:
        model = AI_Insights
        fields = ['username', 'course', 'insight_text', 'insight_type']
