from django.http import HttpResponse # not needed when use render
from polls.models import Question, Choice
#from django.template import loader #not needed when use render
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    #Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html;
    # we use template_name to tell ListView to use our existing "polls/index.html" template.
    context_object_name = 'key_latest_question_list'
    def get_queryset(self):
        #return the last 5 questions
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    #By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html.
    # In our case, it would use the template "polls/question_detail.html".
    # The template_name attribute is used to tell Django to use a specific template name instead of
    # the autogenerated default template name.
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

# Create your views here.
def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    try:
        choice_id = request.POST['choice'] #POST['choice'] will have value="{{choice.id}}" of radio input from detail.html page
        selected_choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):  # Choice object already has DoesNotExist method
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "you did not select the choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,))) ##args should have iterative, so , is required after question.id

#    context = {'key_question': question,} ## this was for dummy
#    return render(request, 'polls/vote.html',context) ## this was for dummy
