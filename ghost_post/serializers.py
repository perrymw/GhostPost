from rest_framework.serializers import HyperlinkedModelSerializer
from ghost_post.models import BoastandRoast

class BoastandRoastSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BoastandRoast
        fields = [
            'id',
            'boast',
            'content',
            'date',
            'total'
        ]