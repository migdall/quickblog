from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Question, Answer, Hero, Saying

import boto3

# Create your views here.


def new_saying(request):
    if request.POST:
        first_name = request.POST.get("firstname")
        if first_name:
            new_saying = Saying.objects.create(first_name=first_name)
            new_saying.save()
            return redirect('/sayings/%s/hero/' % str(new_saying.id))


def set_hero(request, saying_id):
    if request.POST:
        hero_id = request.POST.get("hero")
        if hero_id:
            hero = Hero.objects.get(id=hero_id)
            saying = Saying.objects.get(id=saying_id)
            saying.hero = hero
            saying.save()
            return redirect('/sayings/%s/questions/1/' % str(saying.id))
    c = {}
    saying = Saying.objects.get(id=saying_id)
    heroes = Hero.objects.all()
    c['saying'] = saying
    c['heroes'] = heroes
    return render(request, 'hero.html', c)


def get_question(request, saying_id, question_id):
    c = {}
    saying = Saying.objects.get(id=saying_id)
    hero = saying.hero
    question = Question.objects.get(id=question_id)

    if question and saying and hero:
        c['question'] = question
        c['saying'] = saying
        c['hero'] = hero
        c['next'] = int(question.id) + 1
        return render(request, 'question.html', c)
    else:
        c['saying'] = saying
        c['hero'] = hero
        return render(request, 'done.html', c)


def new_answer(request, saying_id, question_id):
    if request.POST and request.is_ajax():
        pass
