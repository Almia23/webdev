from django.urls import path
from . import views

urlpatterns = [
    path('', views.promo_view),
]