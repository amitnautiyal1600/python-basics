from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


# Create your views here.
@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    user_serialize_data = UserSerializer(users, many=True)
    return Response(user_serialize_data.data)


@api_view(['POST'])
def save_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', "DELETE"])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serialize_data = UserSerializer(user)
        return Response(user_serialize_data.data)

    if request.method == 'PUT':
        user_serialize_data = UserSerializer(user, data=request.data)
        if user_serialize_data.is_valid():
            user_serialize_data.save()
            return Response(user_serialize_data.data, status=status.HTTP_202_ACCEPTED)
        return  Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
