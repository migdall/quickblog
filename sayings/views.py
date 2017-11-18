from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        return render(request, 'question.html', c)


def new_answer(request, saying_id, question_id):
    if request.POST and request.is_ajax():
        return HttpResponse("success")
        new_recording_upload = request.FILES.get("recording")
        s3 = boto3.resource('s3')
        s3.Object('sayings.answers', 'firstvid.webm').put(request.FILES.get('recording'))
        data = new_recording_upload.read()
        build_key_string = "sayings/%s" % new_recording_upload.name
        return_s3_object = s3.Bucket('sayings.answers').put_object(
            Key=build_key_string, Body=data, ContentType=new_recording_upload.content_type)
        return_s3_object.Acl().put(ACL='public-read')
        s3_client = boto3.client('s3')
        return_s3_object_url = s3_client.generate_presigned_url('get_object', Params={
            'Bucket': 'sayings.answers', 'Key': return_s3_object.key}).split("?")[0]

        saying = Saying.objects.get(id=saying_id)

        question = Question.objects.get(id=question_id)
        answer = Answer.objects.create(recording_url=return_s3_object_url, question=question)
        answer.save()
        saying.answers.add(answer)
        return redirect('/sayings/%s/questions/2/' % str(saying_id))
