from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

def home(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        'user/userhome.html',
        context
    )

def login(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        'user/login.html',
        context
    )
