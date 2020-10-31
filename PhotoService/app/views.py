from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import PhotoForm

# Create your views here.


def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'photos': photos})


def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    # user = get_object_or_404(User, title="タイトル名")
    photos = user.photo_set.all().order_by('-created_at')
    return render(request, 'app/users_detail.html', {'user': user, 'photos': photos})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Userインスタンスを作成
        if form.is_valid():
            new_user = form.save()  # ユーザーインスタンスを保存
            input_username = form.cleaned_data['username']
            # cleand_dataという属性で、formに入力された値を取得して変数へ代入している
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(
                username=input_username, passord=input_password)
            # 認証成功時のみ、ユーザーをログインさせる

            if new_user is not None:
                # loginメソッドは、認証ができてなくてもログインさせることができる(上のauthenticateで認証を実行する)
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})


@login_required
def photos_new(request):
