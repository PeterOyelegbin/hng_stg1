from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
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
