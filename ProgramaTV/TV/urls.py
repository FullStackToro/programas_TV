from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('new', views.new),
    path('create', views.create),
    path('<int:op>/edit', views.edit),
    path('<op>', views.show_one),
    path('<op>/update', views.update),
    path('<op>/destroy', views.destroy),


]
