from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Question, Answer
from .forms import AskForm, AnswerForm
def Quest(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    answers = Answer.objects.filter(question=question.pk).order_by('-added_at')[0:10]
    if request.method == 'POST':
    	form = AnswerForm(request.POST)
    	if form.is_valid():
    		answer = form.save()
    		url = answer.question.get_url()
    		return HttpResponseRedirect(url)
    else:
    	form = AnswerForm(initial={'question': question.pk})
    return render(request, 'qa/question.html', {
    	'question': question,
    	'answers': answers,
    	'form': form,
    	})

def test(request):
	return HttpResponse("OK")


def main_paige(request):
	questions = Question.objects.new()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'qa/main_paige.html',{
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		})

def pop(request):
	questions = Question.objects.popular()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	return render(request, 'qa/popular.html',{
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		})


def Ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'ask.html',{
		'form': form,
		})


# Create your views here.
