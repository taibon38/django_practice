from django.urls import path #DjangoのURL機能であるpath関数をインポート
from .import views #同じ階層にあるviews.pyファイルをインポート

app_name = 'heros'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:hero_id>/',views.detail,name='detail'), #第一引数はURLを指定。
    path('images/',views.image,name='image'),
]
#path関数は、第一引数で空の文字列を指定し、第二引数で、views.indexを指定することで、URL（http://127.0.0.1:8000/）にアクセスした時は、views.pyのindex関数を実行するように設定をしています。
