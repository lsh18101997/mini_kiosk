from django.urls import path, re_path

from . import views

app_name = "kiosk"

urlpatterns = [
    path("", views.MenuLV.as_view(), name="index"),
    path("<slug:slug>", views.MenuDV.as_view(), name="menu_detail"),
    re_path(r'(?P<slug>[-\w]+)/$', views.MenuDV.as_view(), name="menu_detail"),
]