from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import Question, Answer, Hero, Saying

# Create your views here.


def new_saying(request):
    if request.POST:
        first_name = request.POST.get("firstname")
        new_saying = Saying.objects.create(first_name=first_name)
        new_saying.save()
        return redirect('/sayings/%s/hero/' % str(new_saying.id))


@csrf_protect
def set_hero(request, saying_id):
    c = {}
    saying = Saying.objects.get(id=saying_id)
    c['saying'] = saying
    return render(request, 'hero.html', c)

