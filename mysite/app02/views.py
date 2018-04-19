# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from app02 import log
# Create your views here.

def index(request):
    log.info('hello')
    return HttpResponse('app02')

