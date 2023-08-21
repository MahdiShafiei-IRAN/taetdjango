from . import views
from django.urls import path

urlpatterns = [
    path("",views.HomePage.as_view(),name="home"),
    path("tmp/",views.TmpPage.as_view(),name="tmp"),
]
