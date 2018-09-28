from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_auth.views import LogoutView

class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))

class ProfileView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        # return Response(request.user.profile.bio)
        return JsonResponse({"fname":request.user.first_name,"bio":request.user.profile.bio})

class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)
