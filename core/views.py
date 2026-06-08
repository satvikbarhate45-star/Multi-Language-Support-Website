from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.translation import activate


def home(request):
    return render(request, 'home.html')


def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')

        if language in dict(settings.LANGUAGES):
            activate(language)
            request.session['django_language'] = language

    return redirect('home')