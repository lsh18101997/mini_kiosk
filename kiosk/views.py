from django.shortcuts import render
from kiosk.models import Menu
from django.views.generic import ListView, DetailView

class MenuLV(ListView):
    model = Menu
    context_object_name = 'menus'
    template_name = 'kiosk/menu_list.html'
    paginate_by = 10

class MenuDV(DetailView):
    model = Menu
    context_object_name = 'menu'
    template_name = 'kiosk/menu_detail.html'


