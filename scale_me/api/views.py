from django.http import HttpResponse
from django.http import JsonResponse

from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the API index.")

def detail(request, question_id):
    my_question = Question.objects.get(pk=question_id)
    return JsonResponse({'text':my_question.question_text})
