from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^Home/$', views.Home, name="home"),
    url(r'^categories/$', views.categorylist, name="categorylist"),
]
