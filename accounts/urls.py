from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from .forms import LoginForm

urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login_form.html'), name='login',
            kwargs={
                'authentication_form': LoginForm,
                    }),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),
    re_path(r'^profile/$', views.profile, name='profile'),
]
