# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from app01 import log
from app01.other import do_something

# Create your views here.

def index(request):
    log.info('hello')
    do_something()
    return HttpResponse('app01')

