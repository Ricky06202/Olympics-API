from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import OlympicsData
from .serializers import OlympicsSerializer, UserSerializer, User

from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

class OlympicsViewSet(viewsets.ModelViewSet):
    queryset = OlympicsData.objects.all()
    serializer_class = OlympicsSerializer

@api_view(['Post'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, create = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['Post'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request): 
    serializer = UserSerializer(instance=request.user)
    # serializer2 = OlympicsSerializer(OlympicsData)
    return Response(serializer.data, status=status.HTTP_200_OK)

    # return Response("Estas logeado {}".format(request.user.username), status=status.HTTP_200_OK)
    # serializer2 = OlympicsSerializer()



# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def olympics_data(request):
#     serializer = OlympicsSerializer(OlympicsData) 
#     return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def olympics_data(request):
    if request.method == 'GET':
        olympic_events = OlympicsData.objects.all()  
        serializer = OlympicsSerializer(olympic_events, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  # Handle non-GET requests


    # if serializer.is_valid():
    #     olymicspData = request.user.OlympicsData
    #     serializer = OlympicsSerializer(olymicspData)
    #     return Response (serializer.data)
