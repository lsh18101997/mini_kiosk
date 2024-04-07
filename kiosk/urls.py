from django.urls import path, re_path

from . import views

app_name = "kiosk"

urlpatterns = [
    path("", views.MenuLV.as_view(), name="index"),
    path("<int:menu_id>", views.order, name="index2"),
    re_path(r'(?P<slug>[-\w]+)/$', views.MenuDV.as_view(), name="menu_detail"),
]