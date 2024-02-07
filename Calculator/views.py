import json

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def calculate_expression(request):
    method = request.method
    if method == "POST":
        data = json.loads(request.body)
        print(data)

        # 从JSON数据中获取表达式
        expression = data.get('expression')

        try:
            result = calculate(expression)
            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Invalid Method'}, status=400)



def init(request):
    return render(request, "cal.html")


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

# if __name__ == '__main__':
#     a = "123+456"
#     b = a.split("+")
#     c = a.split()
#     print(c)