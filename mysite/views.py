from django.shortcuts import render,redirect
from django.http import HttpResponse
import random 
from mysite.models import News, Animal
#帳密: admin p33065286
def index(request):
    #lotto = [random.randint(1,49) for i in range(6)]
    if request.method=="POST":
        #判斷資料是否進入
        title = request.POST.get("title")
        item = News(title = title)
        item.save()
        return redirect("/")

    lotto = [n for n in range(1,49)]
    random.shuffle(lotto)
    lotto = lotto[0:6]
    news = News.objects.all().order_by('-pdate')
    return render(request,"index.html",locals()) 

def delete(request,id):
    target = News.objects.get(id=id)
    target.delete()
    return redirect("/")

def animal(request):
    animals = Animal.objects.all().order_by('-update')
    return render(request,"animal.html",locals())
