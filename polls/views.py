from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    recent_qs = Question.objects.order_by('-pub_date')[:5]
    context = {'recent_qs': recent_qs}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    return render(request, 'polls/vote.html', {'question': question})
