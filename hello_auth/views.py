from django.shortcuts import render


def index(request, template='hello_auth/base.html'):
    return render(request, template)
