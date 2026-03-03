from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def register(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not name or not email or not password :
        return Response({
            "success" : False,
            "message" : "All fields are required.",
            "statuscode" : 400
        }, status.HTTP_400_BAD_REQUEST)
    return Response({
        "success" : True,
        "message" : "Registeraton successful.",
        "data_recieved" : request.data
    }, status.HTTP_201_CREATED)