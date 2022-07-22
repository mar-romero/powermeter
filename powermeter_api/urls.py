from django.contrib import admin
from django.urls import path

from powermeter_api.views import mediciones_list, mediciones_create,mediciones_max,mediciones_min,mediciones_averge,mediociones_delete

urlpatterns = [
    path('save/',mediciones_create),
    path('list/',mediciones_list),
    path('max/',mediciones_max),
    path('min/',mediciones_min),
    path('avg/',mediciones_averge),
    path('<int:pk>',mediociones_delete)

]