from django import forms
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post  # モデルをインポート
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html', {
            'post_data': post_data
        })


class PostDetailView(View):  # 詳細を表示
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)  # PostFormをコールする。importが必要
        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        """
        ボタンをクリックした時にコールされる関数
        """
        form = PostForm(request.POST or None)  # PostFormをコールする。importが必要

        if form.is_valid():  # postの中身をチェック
            post_data = Post()  # チェックが通ったら、Postモデルをpost_dataへ格納
            post_data.author = request.user  # authorへ、ログインユーザを代入
            # formの内容を取得して、タイトルへ代入。
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()  # データベースへ保存
            return redirect('post_detail', post_data.id)

        return render(request, 'app/post_form.html', {
            'form': form
        })  # postの内容にエラーがあれば、投稿フォームを表示


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])  # urlからidを取得。
        form = PostForm(
            request.POST or None,
            initial={  # initialでフォームの初期値を設定。。すでにある投稿の内容を表示させる。
                'title': post_data.title,
                'content': post_data.content
            }
        )
        return render(request, 'app/post_form.html', {
            'form': form
        })  # テンプレートに、formの値を渡している。テンプレート内でformを入力すれば値が表示される

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)  # PostFormをコールする。importが必要

        if form.is_valid():  # postの中身をチェック
            # チェックが通ったら、Postモデルから特定のデータを取得
            post_data = Post.objects.get(id=self.kwargs['pk'])
            # formの内容を取得して、タイトルへ代入。
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()  # データベースへ保存
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_form.html', {
            'form': form
        })  # postの内容にエラーがあれば、投稿フォームを表示


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # urlからidを取得して、特定のPostデータを取得する
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {  # renderでテンプレートへpost_dataを渡す。
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        # urlからidを取得して、特定のPostデータを取得する
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')
