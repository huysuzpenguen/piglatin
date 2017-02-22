from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',locals())

def translate(request):
    originalText = request.GET['txtOriginalText'].lower()
    translationText = ''
    for word in originalText.split():
        if word[0] in ['a','e','i','o','u']:
            translationText += word
            translationText += 'yay '
        else:
            translationText += word[1:]
            translationText += word[0]
            translationText += 'ay '

    return HttpResponse(translationText)
