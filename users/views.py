from django.shortcuts import render
from django.http import JsonResponse
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.values()
    return JsonResponse(list(users), safe=False)

