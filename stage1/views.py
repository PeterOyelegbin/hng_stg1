from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
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


@csrf_exempt
@api_view(['POST'])
def arithOp(request):
    data = request.data
    x = int(data['x'])
    opr = data['operation_type']
    y = int(data['y'])
    if opr == "+":
        result = x + y
    elif opr == '-':
        result = x - y
    elif opr == '*':
        result = x * y
    elif opr == '/':
        result = x / y
    else:
        result = 'invalid operation type'
    return_data = [
        {
            "slackUsername": "Peter Oyelegbin",
            "result": result,
            "operation_type": str(x) + opr + str(y)
        }   
    ]
    return Response(return_data, status=status.HTTP_202_ACCEPTED)

