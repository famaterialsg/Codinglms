from django.db import models
from user.models import User
from subject.models import Subject

class AI_Insights(models.Model):    
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    # course = models.CharField(max_length=255)
    course = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    insight_text = models.CharField(max_length=255, blank=True, null=True)
    insight_type = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.course} - {self.insight_text} - {self.insight_type} "