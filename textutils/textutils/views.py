#This file is created by Akshat 
from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
      
      return render(request,'index.html')
    # return HttpResponse('<h1>Home</h1><a href="https://www.monsterindia.com/career-advice/python-oops-interview-questions/">Python</a>')

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    charactercount=request.POST.get("charactercount",'off')
    #analyze the text
    if removepunc=="on":
     analyze=""
     punctuations='''!(){}[]-;:"'\,<>./?@#$%^&*_~'''
     for char in djtext:
        if char not in punctuations:
            analyze=analyze+char
     #params={'purpose':'Remove punctuations',"analyzed_text":analyze}
     #return render(request,'analyze.html',params)
     djtext=analyze
    if fullcaps=="on":
        analyze=""
        for char in djtext:
            analyze=analyze+char.upper()
        #params={'purpose':'Uppercase',"analyzed_text":analyze}
        #return render(request,'analyze.html',params)
        djtext=analyze
    if newlineremover=='on':
        analyze=""
        for char in djtext:
          if char!='\n':
            analyze=analyze+char
        #params={'purpose':'New Line Remove',"analyzed_text":analyze}
        #return render(request,'analyze.html',params)
        djtext=analyze
    if charactercount=='on':
        c=0
        for words in djtext:
          for chars in words:
            if chars==None:
                pass
            if chars==" ":
                pass
            else:
                c=c+1
        params={'purpose':'Charactercount',"analyzed_text":c}
        return render(request,'analyze.html',params)
    if (removepunc!='on' and fullcaps!="on" and newlineremover!="on" and charactercount!="on"):
        return HttpResponse("Please Select any option and try again!")
    params={'purpose':'Charactercount',"analyzed_text":analyze}
    return render(request,'analyze.html',params)


