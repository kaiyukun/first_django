from django.shortcuts import render

# HTTPResponseというクラスをインポート
from django.http import HttpResponse

from . import forms
from django.views.generic import TemplateView

# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# View関数を任意に定義
def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'first_django_app_HTML/index.html',context=params)

class FormView(TemplateView):

    # 初期変数定義
    def __init__(self):
        self.params = {
            "Message":"情報を入力してください。",
            "form":forms.Contact_Form(),
        }

    # GET時の処理を記載
    def get(self,request):
        return render(request, "first_django_app_HTML/formpage.html",context=self.params)

    # POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)
            
            # フォーム入力が有効な場合
            if self.params["form"].is_valid():
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "first_django_app_HTML/formpage.html",context=self.params)

class UserFormView(TemplateView):

    #初期変数定義
    def __init__(self):
        self.params = {
            "Message":"情報を入力してください。",
            "form":forms.User_Contact_Form(),
        }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "first_django_app_HTML/user_formpage.html",context=self.params)

    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.User_Contact_Form(request.POST)
            
            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "first_django_app_HTML/user_formpage.html",context=self.params)
    
class PostFormView(TemplateView):

    #初期変数定義
    def __init__(self):
        self.params = {
            "Message":"情報を入力してください。",
            "form":forms.Post_Form(),
        }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "first_django_app_HTML/post_formpage.html",context=self.params)

    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Post_Form(request.POST)
            
            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "first_django_app_HTML/post_formpage.html",context=self.params)
    
#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'first_django_app_HTML/login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "first_django_app_HTML/home.html",context=params)
    
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": forms.AccountForm(),
        "add_account_form":forms.AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = forms.AccountForm()
        self.params["add_account_form"] = forms.AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"first_django_app_HTML/register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = forms.AccountForm(data=request.POST)
        self.params["add_account_form"] = forms.AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"first_django_app_HTML/register.html",context=self.params)