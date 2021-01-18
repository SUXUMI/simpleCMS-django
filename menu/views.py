from django.shortcuts import render
# from . import models
from .models import Menu

def get_menu_items(request):
    return Menu.objects.all()