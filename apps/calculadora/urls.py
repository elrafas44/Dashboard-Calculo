from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("factorial/<int:numero>/", views.factorial_view, name="factorial"),
    path("potencia/<int:base>/<int:exponente>/", views.potencia_view, name="potencia"),
    path("raiz/<int:numero>/", views.raiz_view, name="raiz"),
]
