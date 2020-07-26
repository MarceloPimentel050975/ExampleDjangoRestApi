from django.urls import path

from . import views

urlpatterns = [
    path('', views.endereco_list),
    path('<int:pk>', views.endereco_detail)
]