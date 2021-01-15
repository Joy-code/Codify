from django.shortcuts import render
from django.http import HttpResponse

from .models import codingQ, Attempt, Category, Difficulty


def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def reminders(request):
    return render(request, 'reminders.html')


def stats(request):
    # Generate counts of the total number of codingQs
    num_questions = codingQ.objects.all().count()
    num_attempts = Attempt.objects.all().count()

    context = {
        'num_questions': num_questions,
        'num_attempts': num_attempts,
    }

    return render(request, 'stats.html', context=context)