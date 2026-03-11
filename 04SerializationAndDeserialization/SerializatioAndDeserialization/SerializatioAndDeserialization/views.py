from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(["GET"])
def healthcheck(request):
    return JsonResponse({
        'statuscode' : 200,
        'success':True,
        'message':'Healthcheck successful.'
    })