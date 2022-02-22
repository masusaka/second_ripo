from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,UserManager
)

from django.urls import reverse_lazy

class UserManager(BaseUserManager):   #カスタムマネージャー
    #通常ユーザーを作成する場合の関数を定義、ログインするための設定
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):  #カスタムユーザーを作成、ユーザー名以外でログインしたい時
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)           #ログインの可否
    is_staff = models.BooleanField(default=False)           #管理画面のアクセス可否

    USERNAME_FIELD = 'username'                                #emailでログイン認証したいので、emailをユニークなフィールドとして指定
    #REQUIRED_FIELDS = ['username']

    objects = UserManager() #importしたUserManagerを指定

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')