from rest_framework import viewsets

from ghost_post.models import BoastandRoast
from ghost_post.serializers import BoastandRoastSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})

class PostView(viewsets.ModelViewSet):
    queryset = BoastandRoast.objects.all()
    serializer_class = BoastandRoastSerializer

