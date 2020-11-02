from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from app.models import Product

# Create your models here.


class UserManager(BaseUserManager):
    """カスタムユーザーマネージャー"""  # DjangoのBaseUserManagerクラスの実装を基本的に利用しており、emailによるユーザー認証などを必要な部分だけ書き換えている。
    use_in_migrations = True  # マイグレーションで管理できる。

    def _create_user(self, email, password, **extra_fields):
        # emailを必須にする
        if not email:
            raise ValueError('The given email must be set')
        # email でUserモデルを作成
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    # BaseUserManagerで定義されている関数にオーバーライドしている。
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        return self._create_user(email, password, **extra_fields)

# PermissionMixin は、Djangoにおける権限管理まわりの機能を追加してくれるクラス


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    initial_point = 50000
    email = models.EmailField("メールアドレス", unique=True)
    point = models.PositiveIntegerField(default=initial_point)
    fav_products = models.ManyToManyField(
        Product, blank=True)  # お気に入りを登録。Productモデル
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"  # ユーザーを一意に判別するためのusernameという属性をメールアドレスに置き換えている
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []  # createsuperuser を⾏うときに必須となるフィールドを指定できる。

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
