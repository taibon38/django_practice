from django.contrib import admin
from .models import Hero

# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display=('id','title','created_datetime','image') #指定したフィールドが管理ページに表示される
    list_display_links =('id','title','image')#list_display_linksで指定したフィールドはリンクがつくようになります。

admin.site.register(Hero,HeroAdmin) 
#第１引数：インポートしたHeroモデルを、Adminページで利用できるように設定
#第２引数：フィールドを自由に追加
