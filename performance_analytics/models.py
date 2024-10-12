from django.db import models
from course.models import Course
from quiz.models import Quiz
from user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class PerformanceAnalytics(models.Model):
    analy_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    average_score = models.FloatField(default=0.0)
    completion_rate = models.FloatField(default=0.0)

    def update_performance(self):
        quizzes = Quiz.objects.filter(user_id=self.user_id, course_id=self.course_id)
        total_quizzes = quizzes.count()
        if total_quizzes > 0:
            total_score = quizzes.aggregate(models.Sum('score'))['score__sum'] or 0
            self.average_score = total_score / total_quizzes
            completed_quizzes = quizzes.filter(score__gt=0).count()
            self.completion_rate = completed_quizzes / total_quizzes
        else:
            self.average_score = 0.0
            self.completion_rate = 0.0
        self.save()
    
    class Meta:
        db_table = 'performance' 

@receiver(post_save, sender=Quiz)
def update_performance_analytics(sender, instance, **kwargs):
    try:
        performance = PerformanceAnalytics.objects.get(user_id=instance.user_id, course_id=instance.course_id)
    except PerformanceAnalytics.DoesNotExist:
        performance = PerformanceAnalytics(user_id=instance.user_id, course_id=instance.course_id)
    performance.update_performance()