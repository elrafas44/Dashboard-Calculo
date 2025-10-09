from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("factorial/<int:numero>/", views.factorial_view, name="factorial"),
    path("potencia/<int:base>/<int:exponente>/", views.potencia_view, name="potencia"),
    path("raiz/<int:numero>/", views.raiz_view, name="raiz"),
    path("suma/<str:num1>/<str:num2>/", views.suma_view, name="suma"),
    path("resta/<str:num1>/<str:num2>/", views.resta_view, name="resta"),
    path("multiplicacion/<str:num1>/<str:num2>/", views.multiplicacion_view, name="multiplicacion"),
    path("division/<str:num1>/<str:num2>/", views.division_view, name="division"),
]
