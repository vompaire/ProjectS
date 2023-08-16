from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from allauth.account.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),  # Попадание в админку
    path('news/', include('newsapp.urls')),  # На сайт с новостями
    path('', TemplateView.as_view(template_name='default.html'), name='home'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('protect/', include('protect.urls')),
    path('auth/google/', include('social_django.urls', namespace='social')),
    path('', include('userprofile.urls'))
]
