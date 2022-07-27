from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
import jwt,datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter

# Create your views here.
class CreateDonateur(generics.CreateAPIView):
    queryset=DonateurUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=DonateurMSerializer

class CreateDonateurOr(generics.CreateAPIView):
    queryset=DonateurUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=DonateurOrSerializer

class EffectuerDons(generics.ListCreateAPIView):
    queryset=EffectuerDon.objects.all()
    permission_classes=[AllowAny]
    serializer_class=EffectuerSerializer

class ListDonateur(generics.RetrieveUpdateDestroyAPIView):
    queryset=DonateurUser.objects.all()
    permission_classes=[AllowAny]
    serializer_class=EffectuerSerializer

class ListDon(generics.RetrieveUpdateDestroyAPIView):
    queryset=EffectuerDon.objects.all()
    permission_classes=[AllowAny]
    serializer_class=EffectuerSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer