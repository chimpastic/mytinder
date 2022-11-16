from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import models


class HelloApiView(APIView):

    """Example api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = ['sbvkj', 'sdvjbds', 'sdjjdsv']

        return Response({'message': 'this is an api view', 'api': an_apiview})

    def post(self, request):
        """create a hello msg with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'hello {name}'
            return Response({'msg': msg})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloApiViewset(viewsets.ViewSet):

    """An exmaple viewset"""

    def list(self, request):
        a_viewset = [
            'sdfsfsdf', 'sdfsddsf', 'sdfsdfsdf'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and and updating viewset"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)

    permission_classes = (permissions.updateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating, reading, and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permissions_classes = (
        permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """sets the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)
