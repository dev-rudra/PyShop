from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello Products')


def new(request):
    return HttpResponse('New products')


def single(request):
    return HttpResponse('Single Product')