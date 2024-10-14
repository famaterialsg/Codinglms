from django.db import models
from user.models import User
from subject.models import Subject
# Create your models here.
class PerformanceAnalytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    completion_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    predicted_performance = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Performance_Analytics'
    # def __str__(self):
    #     return f"Analytics {self.analytics_id}" #- User {self.user_id}, Course {self.course_id}