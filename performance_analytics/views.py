from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import PerformanceAnalytics
from .forms import PerformanceAnalyticsForm
from Course_Completion.models import CourseCompletion
import time
# Create your views here.

# def PerformanceAnalytics_list(request):
#     # analytics = PerformanceAnalytics.objects.all()
#     # print('analytics: ',analytics)
#     # return render(request, 'PerformanceAnalytics_list.html',{'analytics' : analytics} )


def PerformanceAnalytics_list(request):
    try:
        analytics = PerformanceAnalytics.objects.all()
        return render(request, 'PerformanceAnalytics_list.html', {'analytics': analytics})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    
# def PerformanceAnalytics_add(request):

#     if request.method == 'POST':
#         form = PerformanceAnalyticsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Performance_Analytics:PerformanceAnalytics_list')
#     else:
#         form = PerformanceAnalyticsForm()

#     return render(request, 'PerformanceAnalytics_form.html', {'form':form})

def PerformanceAnalytics_edit(request,pk):
    analytics = get_object_or_404(PerformanceAnalytics, pk=pk)
    if request.method == "POST":
        form = PerformanceAnalyticsForm(request.POST, instance=analytics)
        if form.is_valid():
            form.save()
            return redirect('Performance_Analytics:PerformanceAnalytics_list')
    else:
        form = PerformanceAnalyticsForm(instance=analytics)
    return render(request, 'PerformanceAnalytics_form.html', {'form':form})

def PerformanceAnalytics_detail(request, pk):
    try:
        analytics = get_object_or_404(PerformanceAnalytics, pk=pk)  
        return render(request, 'PerformanceAnalytics_detail.html', {'analytic':analytics})
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    

def PerformanceAnalytics_add(request):

    if request.method == 'POST':
        form = PerformanceAnalyticsForm(request.POST)
        if form.is_valid():
            performance_analytics = form.save()
            user_id = performance_analytics.user_id
            course_id = performance_analytics.course_id

            course_completion = CourseCompletion(
                user_id=user_id,
                course_id=course_id,
                completion_date=time.localtime(time.time())  # Hoặc sử dụng giá trị mặc định
            )
            course_completion.save()

            return redirect('Performance_Analytics:PerformanceAnalytics_list')
    else:
        form = PerformanceAnalyticsForm()

    return render(request, 'PerformanceAnalytics_form.html', {'form':form})