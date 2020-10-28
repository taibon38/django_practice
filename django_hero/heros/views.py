from django.shortcuts import render
from .models import Hero

# Create your views here.

#一言でいうと書き関数は、ユーザーからのリクエストをもとに、index.htmlを返す関数
def index(request): #requestとは、ユーザーがURLを入力してサーバーにアクセスする時に送られる情報のこと。requestには、例えばログインしている人のユーザー情報などの様々な情報が含まれています。
    heros = Hero.objects.order_by('-created_datetime')
    return render(request,'heros/index.html',{'heros':heros}) 
    #renderメソッドは、request情報を元にしてindex.htmlを表示することを意味しています。renderは[与える・提供する]という意味があります。
    #第３引数は、テンプレート（HTML）に渡したいデータを自由に定義可能。辞書型と同様に定義するため、キーと値を書く。
    #今回は、キーが'heros' 値がheros。→index.htmlでは、herosでクエリセットが表示できる。

def detail(request,hero_id):
    hero = Hero.objects.get(id=hero_id)
    return render(request,'heros/detail.html',{'hero':hero})

def image(request): #requestとは、ユーザーがURLを入力してサーバーにアクセスする時に送られる情報のこと。requestには、例えばログインしている人のユーザー情報などの様々な情報が含まれています。
    return render(request,'django_hero/images') 