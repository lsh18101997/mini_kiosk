from django.shortcuts import render, get_object_or_404
from kiosk.models import Menu
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect



class MenuLV(ListView):
    model = Menu
    context_object_name = 'menus'
    template_name = 'kiosk/menu_list.html'
    paginate_by = 12

class MenuDV(DetailView):
    model = Menu
    context_object_name = 'menu'
    template_name = 'kiosk/menu_detail.html'

def order(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    menu.inventory -= 1
    menu.save()

    return HttpResponseRedirect(reverse("kiosk:index"))
        




