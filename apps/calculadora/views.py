from django.http import JsonResponse
import math

# Vista principal temporal
def home(request):
    return JsonResponse({"mensaje": "Bienvenido al Dashboard de Cálculo - Backend en funcionamiento 🚀"})

# Función factorial
def factorial_view(request, numero: int):
    try:
        resultado = math.factorial(numero)
        return JsonResponse({"operacion": "factorial", "numero": numero, "resultado": resultado})
    except ValueError:
        return JsonResponse({"error": "El factorial solo está definido para enteros no negativos."})

# Función potencia
def potencia_view(request, base: float, exponente: float):
    resultado = math.pow(base, exponente)
    return JsonResponse({"operacion": "potencia", "base": base, "exponente": exponente, "resultado": resultado})

# Función raíz cuadrada
def raiz_view(request, numero: float):
    if numero < 0:
        return JsonResponse({"error": "No se puede calcular la raíz cuadrada de un número negativo."})
    resultado = math.sqrt(numero)
    return JsonResponse({"operacion": "raiz", "numero": numero, "resultado": resultado})
