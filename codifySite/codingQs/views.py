from django.shortcuts import render
from django.http import HttpResponse

from .models import codingQ, Attempt, Category, Difficulty


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    # Generate counts of the total number of codingQs
    num_questions = codingQ.objects.all().count()
    num_attempts = Attempt.objects.all().count()

    context = {
        'num_questions': num_questions,
        'num_attempts': num_attempts,
    }

    return render(request, 'index.html', context=context)