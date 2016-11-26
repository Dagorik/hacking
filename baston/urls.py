from django.conf.urls import url, include
from django.contrib import admin
from .views import BastonView

urlpatterns = [
    url(r'^post/', BastonView.as_view(), name = "baston-post"),
]
