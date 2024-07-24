from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def analyze(request):
    
    #text val input
    dj_text = request.POST.get("text", "default")               #post method for security so that the data doesn't overload the url

    #accepts the checkbox input - which is on or off
    remove_punc = request.POST.get("removepunc", "off")          
    full_caps = request.POST.get('fullcaps', 'off')
    new_line_remover = request.POST.get('newlineremover', 'off')
    indentation_remover = request.POST.get('spaceremover', 'off')
    char_counter = request.POST.get('charcounter', 'off')
    
    #PUNCTUATION MARK REMOVER
    if remove_punc == "on":
        punctuations = """".,?;:!'"-—()[]}{…/\|_@#$%^&*~`+=<>|"""
        analyzed = ""

        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    
    #UPPER CASE 
    elif full_caps == 'on':
        analyzed = ''
        for char in dj_text:
            analyzed = analyzed + char.upper()
        
        params = {
            "purpose" : "Capitalised the Sentence", 
            "analyzed_text" : analyzed
        }

        return render(request, 'analyze.html', params)

    #NEW LINE REMOVER
    elif new_line_remover == 'on':
        analyzed = ''
        for char in dj_text:
            if char != "\n" and char != "\r":               #carriage return
                analyzed = analyzed + char

        params = {
            "purpose" : "New line char removed",
            "analyzed_text" : analyzed
        }

        return render(request, 'analyze.html', params)
    
    #SPACE REMOVER
    elif indentation_remover == 'on':
        analyzed = ''
        for char in dj_text:
            if char != " ":
                analyzed = analyzed + char

        params = {
            "purpose" : "Indentations removed",
            "analyzed_text" : analyzed
        }

        return render(request, 'analyze.html', params)
    
    #CHAR COUNTER
    elif char_counter == "on":
        analyzed = 0
        for char in dj_text:
            analyzed += 1

        params = {
            "purpose" : "Chars counted",
            "analyzed_text" : analyzed
        }

        return render(request, 'analyze.html', params)

    #NONE option
    else:
        return HttpResponse("ERROR!")