from django.conf.urls import url, include
from .views_api import BastonListado, BastonDetalleView
urlpatterns =[
  url(r'^$', BastonListado.as_view()),
  url(r'^(?P<pk>[0-9]+)/$', BastonDetalleView.as_view()),
]