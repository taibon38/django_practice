from django.shortcuts import render

# Create your views here.

#一言でいうと書き関数は、ユーザーからのリクエストをもとに、index.htmlを返す関数
def index(request): #requestとは、ユーザーがURLを入力してサーバーにアクセスする時に送られる情報のこと。requestには、例えばログインしている人のユーザー情報などの様々な情報が含まれています。
    return render(request,'heros/index.html') 
    #renderメソッドは、request情報を元にしてindex.htmlを表示することを意味しています。renderは[与える・提供する]という意味があります。
