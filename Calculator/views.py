import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError

# Create your views here.
@csrf_exempt
def calculate_expression(request):
    method = request.method
    if method == "POST":
        data = json.loads(request.body)
        # 从JSON数据中获取表达式
        expression = data.get('expression')
        if not expression:
            return JsonResponse({'error': 'No expression provided'}, status=400)

        try:
            result = evaluate_expression(expression)
            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid Method'}, status=400)



def init(request):
    return render(request, "cal.html")



def evaluate_expression(expression):
    allowed_chars = "0123456789.+-*/"
    for char in expression:
        if char not in allowed_chars:
            raise ValidationError("非法字符")

    numbers = expression.split()

def calculate(expression):
    if "+" in expression:
        return plus(expression.split("+"))
    elif "-" in expression:
        return minus(expression.split("-"))
    elif "*" in expression:
        return multiply(expression.split("*"))
    elif "/" in expression:
        return divide(expression.split("/"))
    else:
        raise Exception("请检查公式是否正确")

def plus(expression):
    return eval(expression[0]) + eval(expression[1])
def minus(expression):
    return eval(expression[0]) - eval(expression[1])
def multiply(expression):
    return eval(expression[0]) * eval(expression[1])
def divide(expression):
    return eval(expression[0]) / eval(expression[1])
