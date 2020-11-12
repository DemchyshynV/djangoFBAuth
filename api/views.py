from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_social_oauth2.authentication import SocialAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from .serializers import UserSerializer
# class ASD(JWTAuthentication):


class GetUsersView(APIView):
    serializer_class = UserSerializer
    # authentication_classes = [OAuth2Authentication or SocialAuthentication or JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        data = UserSerializer(self.request.user).data
        return Response(data)
