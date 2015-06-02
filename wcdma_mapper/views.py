from django.shortcuts import render


def index(request):
    return render(request, 'wcdma_mapper/index.html')
