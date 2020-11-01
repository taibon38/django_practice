from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Photo, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login  # ログイン認証で利用
from django.contrib.auth.decorators import login_required  # ログインデコレータとして利用
from .forms import PhotoForm
from django.contrib import messages  # 成功メッセージ表示で利用
from django.views.decorators.http import require_POST  # 削除機能の実装で利用

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
        if form.is_valid():  # valid = 有効という意味
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


@login_required  # @はPythonのデコレータ機能。関数を加工できるもの。 login_requiredは、ユーザーがログイン状態であればphotos_new関数を実行。ログインしていなければログイン画面にリダイレクト（settings.pyで設定したLOGIN_URL)
def photos_new(request):
    if request.method == "POST":
        # 入力された情報からフォーム情報を生成。ファイルを生成する際はrequest.FILES がないと正常にアップロードされない。
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, "投稿が完了しました！")
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = PhotoForm()
    return render(request, 'app/photos_new.html', {'form': form})


def photos_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'app/photos_detail.html', {'photo': photo})


@require_POST  # 削除機能
def photos_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('app:users_detail', request.user.id)


def photos_category(request, category):
    # titleがURLの文字列と一致するCategoryインスタンスを取得
    category = Category.objects.get(title=category)
    # 取得したCategoryに属するPhoto一覧を取得
    photos = Photo.objects.filter(category=category).order_by('-created_at')
    return render(request, 'app/index.html', {'photos': photos, 'category': category})
