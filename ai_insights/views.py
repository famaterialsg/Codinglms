from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import AI_Insights
from .forms import AI_InsightsForm

# User views
def ai_insights_list(request):
    ai_insights = AI_Insights.objects.all()
    return render(request, 'ai_insights_list.html', {'ai_insights': ai_insights})

def ai_insights_detail(request, id):
    ai_insights = AI_Insights.objects.get(id=id)
    return render(request, 'ai_insights_detail.html', {'ai_insights': ai_insights})

def ai_insights_add(request):
    if request.method == 'POST':
        form = AI_InsightsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ai_insights:ai_insights_list')
    else:
        form = AI_InsightsForm()
    return render(request, 'ai_insights_form.html', {'form': form})

def ai_insights_edit(request, id):
    ai_insights = get_object_or_404(AI_Insights, id=id)
    print(ai_insights)
    if request.method == 'POST':
        form = AI_InsightsForm(request.POST, instance=ai_insights)
        if form.is_valid():
            form.save()
            return redirect('ai_insights:ai_insights_list')
    else:
        form = AI_InsightsForm(instance=ai_insights)
    return render(request, 'ai_insights_form.html', {'form': form})

def ai_insights_delete(request, id):
    ai_insight = AI_Insights.objects.get(id=id)
    if request.method == 'POST':
        ai_insight.delete()
        return redirect('ai_insights:ai_insights_list')
    return render(request, 'ai_insights_confirm_delete.html', {'ai_insight': ai_insight})
