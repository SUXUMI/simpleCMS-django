from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('<slug>', views.view, name='view'),
]