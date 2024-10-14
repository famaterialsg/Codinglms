from django.urls import path
from . import views

app_name = 'Performance_Analytics'

urlpatterns = [
    path('analytics/', views.PerformanceAnalytics_list, name = 'PerformanceAnalytics_list'),
    path('analytics/create/', views.PerformanceAnalytics_add, name = 'PerformanceAnalytics_add'),
    path('analytics/edit/<int:pk>', views.PerformanceAnalytics_edit, name='PerformanceAnalytics_edit'),
    path('analytics/detail/<int:pk>', views.PerformanceAnalytics_detail, name='PerformanceAnalytics_detail'),
]