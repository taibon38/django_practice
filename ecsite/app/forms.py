from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # カスタムユーザーモデルを参照する。settings.pyのAUTH_USER_MODELに設定したモデルを呼び出す。どのファイルからでもこの関数によってUserモデルを呼び出せる
        model = get_user_model()
        fields = ('email',)


class AddToCartForm(forms.Form):
    num = forms.IntegerField(
        label='数量',
        min_value=1,
        required=True)


class PurchaseForm(forms.Form):  # 郵便番号と住所を入力し、内容に問題なければ実際に決済の処理を行い、Saleモデルに決済情報を追加する。
    zip_code = forms.CharField(
        label='郵便番号',
        max_length=7,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '数字7桁(ハイフンなし)'})
    )
    address = forms.CharField(
        label='住所',
        max_length=100,
        required=False
    )
