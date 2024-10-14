from django.db import models
from user.models import User
from subject.models import Subject
from assignment.models import Assignment

class StudentPerformance(models.Model):
    performance_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)  # No foreign key constraint
    course_id = models.ForeignKey(Subject, on_delete=models.CASCADE)  # No foreign key constraint
    quiz_id = models.IntegerField(null=True, blank=True)  # Optional quiz reference, no foreign key
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE,null=True, blank=True)  # Optional assignment reference, no foreign key
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.performance_id)
