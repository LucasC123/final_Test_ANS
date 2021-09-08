from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ValidateSerializer, RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginApiView(ObtainAuthToken):
    serializer_class = ValidateSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
