from django.forms import ModelForm #Djangoがデフォルトで用意しているModelFormというものをインポート
from .models import Memo

class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['title','text']

#ModelFormは各々のモデルに対応したフォームを作ってくれます。
#今回の場合は、model=MemoとすることでMemoモデルに対応したフォームを生成しています。