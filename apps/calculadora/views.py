from django.shortcuts import render 
from django.http import JsonResponse
import math
from decimal import Decimal, InvalidOperation
import re

# Vista principal temporal
def index(request):
    return render(request, 'calculadora/index.html')

# Función factorial
def factorial_view(request, numero):
    try:
        numero = int(numero)
    except ValueError:
        return JsonResponse({"error": "El valor debe ser un número entero."})
    if numero < 0:
        return JsonResponse({"error": "El factorial solo está definido para enteros no negativos."})
    MAX_FACTORIAL = 150
    if numero > MAX_FACTORIAL:
        return JsonResponse({"error": f"El número es demasiado grande para calcular el factorial (máximo permitido: {MAX_FACTORIAL})."})
    try:
        resultado = math.factorial(numero)
        return JsonResponse({"operacion": "factorial", "numero": numero, "resultado": str(resultado)})
    except ValueError:
        return JsonResponse({"error": "El factorial solo está definido para enteros, no negativos."})

# Función potencia

def potencia_view(request, base, exponente):
    try:
        base = int(base)
        exponente = int(exponente)

        MAX_BASE = 10_000
        MAX_EXPONENTE = 10_000

        # Validar que no excedan los límites seguros
        if abs(base) > MAX_BASE or abs(exponente) > MAX_EXPONENTE:
            return JsonResponse({
                "error": f"Los números son demasiado grandes para calcular (límite base ±{MAX_BASE}, exponente ±{MAX_EXPONENTE})"
            })

        # Calcular potencia
        resultado = base ** exponente

        return JsonResponse({"resultado": str(resultado)})

    except OverflowError:
        return JsonResponse({"error": "El resultado es demasiado grande para representarse"})
    except ValueError:
        return JsonResponse({"error": "Los parámetros deben ser enteros"})
    except Exception as e:
        return JsonResponse({"error": f"Error inesperado: {str(e)}"})




# Función raíz cuadrada
def raiz_view(request, numero):
    try:
        numero = float(numero)
    except ValueError:
        return JsonResponse({"error": "El valor debe ser numérico."})
    if numero < 0:
        return JsonResponse({"error": "No se puede calcular la raíz cuadrada de un número negativo."})
    resultado = math.sqrt(numero)
    resultado_str = format(resultado, 'f')
    return JsonResponse({"operacion": "raiz", "numero": numero, "resultado": resultado_str})

# Función suma
def suma_view(request, num1: str, num2: str):
    pattern = r'^[+-]?\d*\.?\d+$'
    if not re.fullmatch(pattern, num1) or not re.fullmatch(pattern, num2):
        return JsonResponse({"error": "Solo se permiten números, + y -."})
    try:
        num1 = Decimal(num1)
        num2 = Decimal(num2)
    except InvalidOperation:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    resultado = num1 + num2
    resultado_str = format(resultado, 'f')
    return JsonResponse({"operacion": "suma", "num1": str(num1), "num2": str(num2), "resultado": resultado_str})

def resta_view(request, num1: str, num2: str):
    pattern = r'^[+-]?\d*\.?\d+$'
    if not re.fullmatch(pattern, num1) or not re.fullmatch(pattern, num2):
        return JsonResponse({"error": "Solo se permiten números, + y -."})
    try:
        num1 = Decimal(num1)
        num2 = Decimal(num2)
    except InvalidOperation:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    resultado = num1 - num2
    resultado_str = format(resultado, 'f')
    return JsonResponse({"operacion": "resta", "num1": str(num1), "num2": str(num2), "resultado": resultado_str})

def multiplicacion_view(request, num1: str, num2: str):
    pattern = r'^[+-]?\d*\.?\d+$'
    if not re.fullmatch(pattern, num1) or not re.fullmatch(pattern, num2):
        return JsonResponse({"error": "Solo se permiten números, + y -."})
    try:
        num1 = Decimal(num1)
        num2 = Decimal(num2)
    except InvalidOperation:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    resultado = num1 * num2
    resultado_str = format(resultado, 'f')
    return JsonResponse({"operacion": "multiplicacion", "num1": str(num1), "num2": str(num2), "resultado": resultado_str})

def division_view(request, num1: str, num2: str):
    pattern = r'^[+-]?\d*\.?\d+$'
    if not re.fullmatch(pattern, num1) or not re.fullmatch(pattern, num2):
        return JsonResponse({"error": "Solo se permiten números, + y -."})
    try:
        num1 = Decimal(num1)
        num2 = Decimal(num2)
    except InvalidOperation:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    if num2 == 0:
        return JsonResponse({"error": "No se puede dividir por cero."})
    resultado = num1 / num2
    resultado_str = format(resultado, 'f')
    return JsonResponse({"operacion": "division", "num1": str(num1), "num2": str(num2), "resultado": resultado_str})
