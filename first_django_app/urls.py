#path関数をインポート
from django.urls import path
# 同ディレクトリからview.pyをインポート
from . import views

#path関数(アクセスするアドレス、呼び出す処理)を追記
urlpatterns = [
    path('index', views.index, name='index'),
    path('formpage', views.FormView.as_view(),name="formpage"),
    path('post_formpage', views.PostFormView.as_view(),name="post_formpage"),
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
]