from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

def get_users(request):
    users = User.objects.all().values("id", "name", "email")
    return JsonResponse(list(users), safe=False)

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = User.objects.create(name=data["name"], email=data["email"])
            return JsonResponse({"message": "User created!", "user_id": user.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
