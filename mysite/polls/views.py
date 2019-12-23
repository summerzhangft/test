from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404,render


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
   # output = ','.join([question.question_text for question in last_question_list])
    context = {
              'last_question_list' : last_question_list, 
          }
    return HttpResponse(template.render(context, request))


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question}) 

def results(request,question_id):
    reponse = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
    
    
# Create your views here.
