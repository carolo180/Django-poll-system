from multiprocessing import context
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Question, Choice, Vote


def home(request): #polls
    polls = Question.objects.all()
    choices = Choice.objects.all()

    context = {
        'polls': polls,
        'choices': choices,
    }

    return render(request, "poll/home.html", context)

def vote(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    choices = Choice.objects.filter(question_id=poll)
    context = {
        'poll': poll,
        'choices': choices,
    }

    if request.method == 'POST':
        choice_id = request.POST.get('option')
        vote = Vote(choice_id=choice_id)
        vote.save()
        
        return redirect('create')

    return render(request, 'poll/vote.html', context) 

def create(request): 
   
    return render(request, "poll/create.html")


# Create your views here.

def results(request, poll_id):
    poll = Question.objects.get(pk=poll_id)
    choices = Choice.objects.filter(question_id=poll)
    votes = Vote.objects.filter(choice__question=poll)

    
    context = {
        'poll': poll,
        'choices': choices,
        'votes': votes,
    }

    return render(request, 'poll/results.html', context)