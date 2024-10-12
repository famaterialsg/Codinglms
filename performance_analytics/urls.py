from django.urls import path,include
from .views import *

app_name ="performance_analytics"
urlpatterns = [
    path('', view=performance_analytics, name='performance_analytics'),]