from django.shortcuts import render

# Create your views here.
def performance_analytics(request):
    return render(request, 'index.html')