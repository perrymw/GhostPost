from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ghost_post.models import BoastandRoast
from ghost_post.serializers import BoastandRoastSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token


class PostView(viewsets.ModelViewSet):
    queryset = BoastandRoast.objects.order_by("-date")
    serializer_class = BoastandRoastSerializer

    @action(detail=False)
    def roasts_only(self, request):
        queryset= BoastandRoast.objects.filter(boast=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def boasts_only(self, request):
        queryset= BoastandRoast.objects.filter(boast=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest_to_lowest(self, request):
        queryset= BoastandRoast.objects.order_by('-total')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def lowest_to_highest(self, request):
        queryset= BoastandRoast.objects.order_by('total')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def upvotes(self, request, pk=None):
        post = self.get_object()
        post.upordown += 1
        post.total += 1
        post.save()
        return Response({'status': 'upvote'})

    @action(detail=True, methods=['get'])
    def downvotes(self, request, pk=None):
        post = self.get_object()
        post.upordown -= 1
        post.total -= 1
        post.save()
        return Response({'status': 'downvote'})
