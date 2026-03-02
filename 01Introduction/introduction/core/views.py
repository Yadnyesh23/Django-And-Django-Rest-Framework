from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def healthcheck(request):
    return Response({
  "status": "running",
  "service": "production_backend",
  "message": "Backend is working correctly, Hello"
})