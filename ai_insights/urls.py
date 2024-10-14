from django.urls import path
from . import views
app_name = 'ai_insights'

urlpatterns = [
    path('ai_insights/', views.ai_insights_list, name='ai_insights_list'),
    path('ai_insights/<int:id>/', views.ai_insights_detail, name='ai_insights_detail'),
    path('ai_insights/create/', views.ai_insights_add, name='ai_insights_add'),
    path('ai_insights/edit/<int:id>/', views.ai_insights_edit, name='ai_insights_edit'),
    path('ai_insights/delete/<int:id>/', views.ai_insights_delete, name='ai_insights_delete'),
]
