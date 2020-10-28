from django.urls import path
from .import views

app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:memo_id>',views.detail,name='detail'),
    path('new_memo',views.new_memo,name='new_memo'),
    path('delete_memo/<int:memo_id>',views.delete_memo,name='delete_memo'),
    path('edit_memo/<int:memo_id>',views.edit_memo,name='edit_memo')
]
#path関数の第一引数はURLを指定しており、第二引数はそのURLに結びつけるviewを指定してます。この場合、appの中のindexというview関数に紐づけています。name引数はそれぞれのURLに名前を設定しており、他のviewから呼び出すときに利用できる名前になります。

