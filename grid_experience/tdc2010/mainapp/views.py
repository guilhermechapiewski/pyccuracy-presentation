# Create your views here.

import time

from django.http import HttpResponse

def fast_view(request):
    time.sleep(1)
    return HttpResponse('ok fast')

def slow_view(request):
    time.sleep(3)
    return HttpResponse('ok slow')

def slower_view(request):
    time.sleep(5)
    return HttpResponse('ok slower')
