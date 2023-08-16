from allauth.account.forms import SignupForm, LoginForm
from protect.forms import AuthenticationAjaxForm, RegistAjaxForm, ResetAjaxForm


# def registration_form_processor(request):
#     return {'registration_form': SignupForm()}
#
#
# def login_form_processor(request):
#     return {'login_form': LoginForm()}


def get_context_data(request):
    return {'login_ajax': AuthenticationAjaxForm()}


def get_context_dataR(request):
    return {'regist_ajax': RegistAjaxForm()}


def get_context_dataRS(request):
    return {'reset_ajax': ResetAjaxForm()}