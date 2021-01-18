# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def homepage(request):
    # TODO: get first menu item url

    url = reverse('pages:view', args=['home'])
    return redirect(url)
    # return HttpResponse("homepage..")
