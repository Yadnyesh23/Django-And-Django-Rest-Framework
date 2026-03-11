from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
users = [
    {"id": 1, "name": "Rahul", "email": "rahul@gmail.com", "age": 21},
    {"id": 2, "name": "Amit", "email": "amit@gmail.com", "age": 22},
    {"id": 3, "name": "Sneha", "email": "sneha@gmail.com", "age": 20}
]

@api_view(["GET"])
def get_users(request):
    page = request.GET.get("page",2)
    limit = request.GET.get("limit",2)
    
    start = (page - 1) * limit
    end = start + limit 
    
    paginated_users = users[start:end]
    
    return Response({
        "success" : True,
        "statuscode" : 200,
        "message" : "All users fetched successfully.",
        "page" : page,
        "limit" : limit,
        "total_users" : len(users),
        "data" : paginated_users
    })
    
@api_view(["GET"])
def get_user_by_id(request, user_id):
    
    for user in users:
        if user['id'] == int(user_id) :
            return Response({
                "success" : True,
                "statuscode" : 200,
                "message" : f"Fetched user of id : {user_id}",
                "data" : user
            })
        return Response({
            "success" : False,
            "statuscode" : 404,
            "message" : "User not found"
        }, status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_user(request):
    body = json.loads(request.body)
    
    new_user = {
        "id" : len(users) + 1,
        "name" : body.get("name"),
        "email": body.get("email"),
        "age" : body.get("age")
    }
    
    users.append(new_user)
    
    return Response({
        "success" : True,
                "statuscode" : 201,
                "message" : "Created User Successfully.",
                "data" : new_user
    }, status.HTTP_201_CREATED)
    
@api_view(["DELETE"])
def delete_user(request, user_id):
    for user in users:
        if user["id"] == int(user_id) :
            users.remove(user)
            
            return Response({
                "message" : "User deleted successfully"
            })
        