from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import ToDoList
from .serializers import ToDoListSerializer, RegistationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.
class ToDoListViews(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Mymodel = ToDoList.objects.filter(user=request.user)
        serializer = ToDoListSerializer(Mymodel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['user'] =  request.user.id
        serializer = ToDoListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ToDoItemViews(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            Mymodel = ToDoList.objects.get(id=id, user=request.user)
            serializer = ToDoListSerializer(Mymodel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ToDoList.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = []
    def post(self, request):
        return Response({'message': 'Login Success'}, status=status.HTTP_200_OK)



class LogoutView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        return Response({'message': 'Logout Success'}, status=status.HTTP_200_OK)