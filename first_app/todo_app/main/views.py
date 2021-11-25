from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import TodoSerializer
from .models import Todo

@swagger_auto_schema(methods=['POST'], request_body=TodoSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def todo(request):
    if request.method == 'GET':
        objs = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(objs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer =  TodoSerializer(data=request.data)
        if serializer.is_valid():
            
            if 'user' in serializer.validated_data.keys():
                serializer.validated_data.pop('user')
                
            object = Todo.objects.create(**serializer.validated_data, user=request.user)
            serializer = TodoSerializer(object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=TodoSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, todo_id):
   
    try:
        obj = Todo.objects.get(id = todo_id)
    
    except Todo.DoesNotExist:
        data = {
                'status'  : False,
                'message' : "Does not exist"
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(obj)
        
        data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    #Update the profile of the TODO
    elif request.method == 'PUT':
        serializer = TodoSerializer(obj, data = request.data, partial=True) 

        if serializer.is_valid():
        
            serializer.save()

            data = {
                'status'  : True,
                'message' : "Successful",
                'data' : serializer.data,
            }

            return Response(data, status = status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : False,
                'message' : "Unsuccessful",
                'error' : serializer.errors,
            }

            return Response(data, status = status.HTTP_400_BAD_REQUEST)

    #delete the account
    elif request.method == 'DELETE':
        obj.delete()

        data = {
                'status'  : True,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)