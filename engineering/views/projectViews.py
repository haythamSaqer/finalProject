from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# Create your views here.
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..permissions import ProjectAddPermission


class Project(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProjectAddPermission]

    def get_object(self, pk):
        try:
            return Project.objects.get(id=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProjectSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.isActive = False
        snippet.save()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ProjectList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProjectAddPermission]
    def get(self, request  ):
        snippets = Customer.objects.all()
        serializer = ProjectSerializer(snippets, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class CustomersView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = LargeResultsSetPagination