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
