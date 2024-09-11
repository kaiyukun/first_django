from django.db import models

from django.contrib.auth.models import User

# モデルクラスを作成
class People(models.Model):
	# 項目定義
    Name     = models.CharField(max_length=100)       # 文字列
    Tell     = models.IntegerField(blank=True, null=True) # 整数
    Mail     = models.EmailField(max_length=100)        # Email
    Birthday = models.DateField()                         # 日付
    Website  = models.URLField()                         # URL
    FreeText = models.TextField()                        # フリーテキスト

    # テキスト表示
    def __str__(self):
        return self.Name

class Post(models.Model):
    title = models.CharField(max_length=100) 
    context = models.TextField() 
    link = models.URLField()
    regist_date = models.DateField()

    # テキスト表示
    def __str__(self):
        return self.title
    
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username