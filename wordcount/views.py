from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{'hithere':'this is for learning double brackets'})

def about(request):
    return render(request, 'about.html',{'hithere':'this is about page'})

# # urls example
# def eggs(request):
#     return HttpResponse('<h1>Eggs are great</h1>')


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    wordcount={}
    for word in wordlist:
        if word in wordcount:
            wordcount[word] +=1
        else:
            wordcount[word] = 1

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'charts':wordcount.items()})