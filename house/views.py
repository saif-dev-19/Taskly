from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import HouseSerializer
from .models import House
from .permissons import IsHouseManagerOrNone
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsHouseManagerOrNone]

    @action(detail=True, methods=['post'],name="Join",permission_classes=[])
    def join(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = self.request.user.profile
            if user_profile.house is None:
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif(user_profile.house == house.objects.all()):
                return Response({"info":"You are already a member of this house"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"info":"You are already a member of another house."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    @action(detail=True, methods=['post'],name="Leave", permission_classes=[])
    def leave(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = self.request.user.profile
            if user_profile.house == house:
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"info":"You are not a member of this house"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
