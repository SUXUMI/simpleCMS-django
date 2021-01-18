from . import views

def menus(request):
    return {'menus': views.get_menu_items(request)}