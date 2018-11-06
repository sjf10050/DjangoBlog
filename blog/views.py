from django.shortcuts import render
from django.http import HttpResponse
#import models
from blog import models
# Create your views here.
def index(request):
    articleSingle=models.Article.objects.get(id=1) 
    print(articleSingle.title)
    print(articleSingle.content)
  
    return render(request,'index.html',{"name":"Song"})
    #return HttpResponse('hello world\n')
