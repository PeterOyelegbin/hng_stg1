from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
'HNG Task 1 - GET method'
@csrf_exempt
@api_view(['GET'])
def index(request):
    json_res = {
        "slackUsername": "Peter Oyelegbin",
        "backend": True,
        "age": 26,
        "bio": "A HVAC Engineer with over 6 years professional experience, preparing for full transition into Tech having had 2 years experience in Django web app development."
    }
    return Response(json_res, status=status.HTTP_200_OK)


'HNG Task 2 - POST method'
@csrf_exempt
@api_view(['POST'])
def arithOp(request):
    data = request.data
    op_type = data['operation_type'].lower()
    x = int(data['x'])
    y = int(data['y'])
    if op_type in ['addition', 'add', 'plus', '+']:
        result = x + y
    elif op_type in ['subtraction', 'subtract', 'deduct', 'minus', '-']:
        result = x - y
    elif op_type in ['multiplication', 'multiply', 'times', '*']:
        result = x * y
    else:
        result = 'invalid operation type'
    return_data = {
        "slackUsername": "Peter Oyelegbin",
        "result": result,
        "operation_type": op_type
    }   
    return Response(return_data, status=status.HTTP_200_OK)

