import os
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings

from .models import Post
from .forms import PostForm

# Create your views here.

def generate_view_fn(model):
    def view_fn(request, id):
        instance = get_object_or_404(model, id=id)
        instance_name = model._meta.model_name
        template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
        return render(request, template_name, {
            instance_name: instance,
        })
    return view_fn

post_detail = generate_view_fn(Post)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') #namespace:name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')  # namespace:name
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })

def mysum(request, numbers):
    # request: HttpRequest
    # numbers = "1/2/12/123/12312/312/12123"
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
'''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = 'c:\dev\askdjango\gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response