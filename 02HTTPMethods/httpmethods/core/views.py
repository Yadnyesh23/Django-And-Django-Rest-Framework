from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def httpmethod(request):
    if request.method == "GET":
        return Response({
            "method": "GET",
            "message" : "This is Get method. You are fetching data from server."
        })
    if request.method == "POST":
        return Response({
            "method": "POST",
            "message" : "This is Post method. You sent data to server.",
            "data_recieved" : request.data
        })