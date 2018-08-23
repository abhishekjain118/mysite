from django.shortcuts import render
from django.http import HttpResponse # not needed when use render
from polls.models import Question, Choice
#from django.template import loader #not needed when use render
from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
    latest_questions_list = Question.objects.all()
    print(latest_questions_list)
    #output = '*\n '.join([q.question_text for q in latest_questions_list])
    context = {'key_latest_question_list':latest_questions_list,}
    return render(request,'polls/index.html',context)
    #template = loader.get_template('polls/index.html') #this is how you load a template
    #context = {
    #    'key_latest_question_list':latest_questions_list,
    #}#set a context which is a dictionary
    #return HttpResponse(template.render(context,request)) # this is how you render a template for httpresponse
    #return HttpResponse(output)
    #return HttpResponse("Hello, you are in Polls web application")
    #The render() function takes the request object as its first argument, a template name as its
    # second argument and a dictionary as its optional third argument. It returns an HttpResponse
    # object of the given template rendered with the given context.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'key_question': question}
    return render(request, 'polls/detail.html',context)

def result(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'key_question': question,}
    return render(request, 'polls/result.html',context)

def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'key_question': question,}
    return render(request, 'polls/vote.html',context)
