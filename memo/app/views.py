from django.shortcuts import render,redirect
from .models import Memo
from django.shortcuts import get_object_or_404 #get_object_or_404では、存在しないidが指定された場合は404ページを表示します
from .forms import MemoForm


# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request,'app/index.html',{'memos':memos}) 
    #renderの第２引数では、デフォルト設定で、アプリ内のtemplatesディレクトリを自動で参照する設定になっている。
    #そのため、templates/app/index.htmlを自動指定している。

def detail(request,memo_id):
    memo = get_object_or_404(Memo,id=memo_id)
    return render(request,'app/detail.html',{'memo':memo}) #memoで呼び出せる。

def new_memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST) 
        #form.pyで定義したクラスMemoFormからインスタンスを生成。（request.POST)はユーザーがフォームに入力した情報が含まれ、その情報を元にインスタンスを生成。
        if form.is_valid(): #生成されたMemoインスタンスが正しい値を持っているか検証。
            form.save() #入力データを保存。
            return redirect('app:index')
            #urls.pyで定義したpath('',views.index,name='index')を指定。
    else:
        form = MemoForm
    return render(request,'app/new_memo.html',{'form':form})

#forms.pyファイルからMemoFormをインポートして、変数formに代入しています。
#そして、render関数の第３引数でそれをテンプレートに渡すように設定しています。これで、new_memo.htmlでは、{{ form }}という記述でフォームが表示されるようになります。


from django.views.decorators.http import require_POST

@require_POST #POSTメソッドのときだけ削除機能が実行されるようにする
def delete_memo(request,memo_id):
    memo  = get_object_or_404(Memo,id=memo_id)
    memo.delete()
    return redirect('app:index')

def edit_memo(request,memo_id):
    memo = get_object_or_404(Memo,id=memo_id)
    form = MemoForm
    return render(request,'app/edit_memo.html',{'form':form,'memo':memo})
