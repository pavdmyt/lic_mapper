from django.shortcuts import render


def index(request):
    from django.http import HttpResponse
    return HttpResponse("Test launch of WCDMA mapper.")
