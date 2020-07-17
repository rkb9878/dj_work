from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from polls.models import Question, choice


# Create your views here.

def index(request):
    """Creating HttpRespone For index Hello world"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    alldata = Question.objects.all()
    print(alldata)
    output = ",".join(q.question_text for q in latest_question_list)
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list, 'alldata': alldata})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"Question not found {Question.DoesNotExist}")
    return render(request, 'polls/detail.html', {'question': question})


def results(request):
    question=Question.objects.all()
    return render(request, 'polls/results.html', {'data':question})

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,choice.DoesNotExist):
        return  render(request, 'polls/detail.html', {'question':question, 'error_message': "you did't select the choice"})
    else:
        selected_choice.vote+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:detail',args=(question.id,)))
