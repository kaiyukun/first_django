from django import forms
from django.contrib.auth.models import User
from .models import Post, Account

#フォームクラス作成
class Contact_Form(forms.Form):
    Name = forms.CharField(label="名前")                    
    Tell = forms.IntegerField(label="電話番号")
    Mail = forms.EmailField(label="メールアドレス")
    Birthday = forms.DateField(label="生年月日")
    Website = forms.URLField(label="Webサイト")
    FreeText = forms.CharField(widget=forms.Textarea,label="備考")

class Post_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = Post

        #②表示するモデルクラスのフィールドを定義
        fields = ('title','context','link','regist_date')

        #③表示ラベルを定義
        labels = {
            'title':"タイトル",
            'context':"本文",
            'link':"リンク",
            'regist_date':"登校日",
        }

class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name','account_image',)
        labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",}