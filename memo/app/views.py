from django.shortcuts import render
from .models import Memo
from django.shortcuts import get_object_or_404 #get_object_or_404では、存在しないidが指定された場合は404ページを表示します

# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request,'app/index.html',{'memos':memos}) 
    #renderの第２引数では、デフォルト設定で、アプリ内のtemplatesディレクトリを自動で参照する設定になっている。
    #そのため、templates/app/index.htmlを自動指定している。

def detail(request,memo_id):
    memo = get_object_or_404(Memo,id=memo_id)
    return render(request,'app/detail.html',{'memo':memo})

def new_memo(request):
    return render(request,'app/new_memo.html')