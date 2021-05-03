from django.urls import path
from .views import *

urlpatterns = [
    path("", view_index, name="mart_index"),
    path("show/<uuid:pk>", view_show, name="product_show"),
]
