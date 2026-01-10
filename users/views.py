from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,mixins
from users.serializers import UserSerializer
from users.permissions import IsUserOwnerOrGetAndPostOnly,IsProfileOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer



# Generic viewset diye hoy sudu viewset. ar Retrive diye retrive kora jabe, ar update diye update kora jabe 
# kono create ba delete kora jabe na
# ListModelMixin diye list o kora jabe ebong dekha jabe.
class ProfileViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                    #  mixins.CreateModelMixin, mixins.DestroyModelMixin
                     ):  
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly,]
