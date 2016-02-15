from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answer
from theme.models import Theme
from utils import mp_render
import json 
# Create your views here.

def index(request,question_id):
	try:
		question	= Question.objects.get(id=question_id)
		answers		= Answer.objects.filter(question_id=question_id)

		context 	= {}
		context['answers']	= answers
		context['question']	= question
	except:
		return render(request,'404.html')
	else:
		return mp_render(request,'question.html',context)


def question(request,theme_id,question_num=0):
	try:
		theme = Theme.objects.get(id=theme_id)
		question_num = int(question_num)
		if(theme.question_num<=question_num):
			return mp_render(request,'finish.html')
		else:
			questions	= Question.objects.filter(theme_id=theme_id)[question_num:question_num+1]
			for question in questions:pass
			answers		= Answer.objects.filter(question_id=question.id)

			context 	= {}
			context['answers']	= answers
			context['question']	= question
			context['theme_id']	= theme_id
			context['question_num']	= question_num+1
			return mp_render(request,'question.html',context)
	except:
		return render(request,'404.html')		

def addAnswer(request):
	result = {}
	result['status'] = 1
	try:
		answer_id = request.REQUEST.get('answer_id')
		answer = Answer.objects.get(pk=answer_id)
		answer.select_num = answer.select_num + 1
		answer.save()
	except  Exception,e:
		result['status'] = 0
		result['info'] = 'error'
		return HttpResponse(json.dumps(result),content_type="application/json")
	else:
		result['info'] = 'success'
		return HttpResponse(json.dumps(result),content_type="application/json")