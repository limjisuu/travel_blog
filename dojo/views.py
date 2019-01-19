from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, numbers):
    # request: HttpRequest
    # numbers = "1/2/12/123/12312/312/12123"
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)
