from django.contrib import admin
from .models import Post  # 作成したモデルを追加

# Register your models here.

admin.site.register(Post)
