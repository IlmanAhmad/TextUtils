# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # function for navigating to index page url


def home(request):
    return render(request, 'home.html')
    # function for navigating to home page url


def aboutus(request):
    return render(request, 'about.html')
    # function for navigating to about page url


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    #assigning checkbox variables
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspacemover = request.POST.get('extraspacemover', 'off')
    counter = request.POST.get('counter', 'off')


    if removepunc == 'on':                          #if conditions for checkbox values
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed


    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed


    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if(extraspacemover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed


    if(counter=='on'):
        analyzed =""
        i = 0
        for char in djtext:
            if char != " ":
                i = i + 1
                analyzed = i
        params = {'purpose': 'Count of Characters', 'analyzed_text': analyzed}


    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspacemover != 'on' and counter != 'on'):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
