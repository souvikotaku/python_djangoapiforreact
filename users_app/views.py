from .models import User

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse  # Import JsonResponse here
import json


def get_users(request):
    users = User.objects.all()
    data = []
    for user in users:
        data.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
        })
    return JsonResponse(data, safe=False)

@csrf_exempt  # Use with extreme caution!
def user_create(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                name = data.get('name')
                email = data.get('email')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:  # Standard form submission
            name = request.POST.get('name')
            email = request.POST.get('email')

        try:
            user = User.objects.create(name=name, email=email)
            if request.content_type == 'application/json':
                return JsonResponse({'message': 'User created successfully', 'user_id': user.id}, status=201)
            else:
                messages.success(request, 'User created successfully!')
                return redirect('user_list')
        except Exception as e:
            if request.content_type == 'application/json':
                return JsonResponse({'error': str(e)}, status=400)
            else:
                messages.error(request, f'Error creating user: {e}')
                return render(request, 'user_create.html', {'error': str(e)})

    return render(request, 'user_create.html')