from django import forms


class PostForm(forms.Form):  # ブログを投稿する時のフォーム
    title = forms.CharField(max_length=30, label='タイトル')
    # 複数行入力可能なテキストエリアを設定できる。
    content = forms.CharField(label='内容', widget=forms.Textarea())
