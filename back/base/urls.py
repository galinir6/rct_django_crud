"""
app

"""
from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('products', views.products),
    path('products/<int:id>', views.products),

]
