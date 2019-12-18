from rest_framework.serializers import HyperlinkedModelSerializer
from ghost_post.models import BoastandRoast

class BoastandRoastSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BoastandRoast
        fields = [
            'boast',
            'content',
            'date',
            'total'
        ]