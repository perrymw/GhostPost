from rest_framework import viewsets

from ghost_post.models import BoastandRoast
from ghost_post.serializers import BoastandRoastSerializer

class PostView(viewsets.ModelViewSet):
    queryset = BoastandRoast.objects.all()
    serializer_class = BoastandRoastSerializer