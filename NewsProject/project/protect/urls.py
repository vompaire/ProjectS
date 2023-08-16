from django.urls import path

from . import views
from protect.views import LoginAjaxView, ResetAjaxView
from protect.views import RegistAjaxView#, logout_view

urlpatterns = [
    path('regist_ajax/', RegistAjaxView.as_view(), name="regist_ajax"),
    path('login_ajax/', LoginAjaxView.as_view(), name="login_ajax"),
    path('reset_ajax', ResetAjaxView.as_view(), name="reset_ajax"),

]
