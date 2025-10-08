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

# Función suma
def suma_view(request, num1: str, num2: str):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    resultado = num1 + num2
    return JsonResponse({"operacion": "suma", "num1": num1, "num2": num2, "resultado": resultado})

# Función resta
def resta_view(request, num1: str, num2: str):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    resultado = num1 - num2
    return JsonResponse({"operacion": "resta", "num1": num1, "num2": num2, "resultado": resultado})

# Función multiplicación
def multiplicacion_view(request, num1: str, num2: str):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    resultado = num1 * num2
    return JsonResponse({"operacion": "multiplicacion", "num1": num1, "num2": num2, "resultado": resultado})

# Función división
def division_view(request, num1: str, num2: str):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return JsonResponse({"error": "Los valores deben ser numéricos."})
    if num2 == 0:
        return JsonResponse({"error": "No se puede dividir por cero."})
    resultado = num1 / num2
    return JsonResponse({"operacion": "division", "num1": num1, "num2": num2, "resultado": resultado})