from django.urls import path, re_path
from . import views
from . import views_cbv

app_name = 'blog' #에러 나서 구글링 해서 임의로 추가

urlpatterns = [
    re_path(r'^$', views_cbv.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    path('new/', views.post_new, name='post_new'),
    re_path(r'^cbv/new/$', views_cbv.post_new),
]