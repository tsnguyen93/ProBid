from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

def home(request):
    assert isinstance(request, HttpRequest)

    context = RequestContext(request)
    return render(
        request,
        '../../ProBid/templates/user/userhome.html',
        context
    )
