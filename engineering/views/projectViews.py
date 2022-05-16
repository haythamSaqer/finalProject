from datetime import datetime

from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view

from ..tasks import send_feedback_email_task
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..permissions import ProjectAddPermission
from ..models import ProjectTasks, Project


class ProjectDetails(APIView):
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
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [ProjectAddPermission]

    def get(self, request ):
        snippets = Project.objects.all()
        serializer = ProjectSerializer(snippets, many=True)
        send_feedback_email_task.delay("haytham.saqer31@gmail.com", "test")
        print("successfully")
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


class ProjectTask(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProjectAddPermission]

    def get_object(self, pk):
        try:
            return Project.objects.get(id=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProjectTaskSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProjectTaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.isActive = False
        snippet.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectTaskList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProjectAddPermission]

    def get(self, request):
        snippets = ProjectTasks.objects.all()
        serializer = ProjectTaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectTaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# class ProjectTask(APIView):
#     # engineer can access it by , get  ,
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [ProjectAddPermission]
#
#     def get_object(self, pk):
#         try:
#             return ProjectTasks.objects.get(id=pk)
#         except ProjectTasks.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = ProjectTasksSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         print(request.data)
#         serializer = ProjectTasksSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
# class ProjectTaskList(APIView):
#     # supervisor engineer can add it , list , delete , update
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [ProjectAddPermission]
#     def get(self, request  ):
#         snippets = Customer.objects.all()
#         serializer = ProjectTasksSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProjectTasksSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET' , 'OPTIONS'])
# # add the permission guys !!
# def submit_task(request , pk ):
#     project_task = ProjectTasks.objects.get(id=pk)
#     project_task.completedByEmployee = True
#     project_task.save()
#     url = 'http://127.0.0.1:8000/project-task/%s/'%project_task.id
#     send_feedback_email_task.delay(
#         "ismaelalsafadi@protonmail.com", "wenfjnwekfjnwekifdjw")
#     # add async method ...
#     return Response({'status': 'jwefjw'} , status=status.HTTP_200_OK)
#
#
# @api_view(['GET' , 'OPTIONS'])
# def approve_task(request , pk):
#     month = datetime.now().month # not the optimal solution
#     year = datetime.now().year # not the optimal solution
#     project_task = ProjectTasks.objects.get(id=pk)
#     project_task.confirmedBySuperVisor = True
#     project_task.save()
#     print(project_task.employee)
#     emp = Employee.objects.get(employeeID=project_task.employee.employeeID)
#
#     return Response({'status': 'nfjkefflwfw'} , status=status.HTTP_200_OK)
#     # edit approed by supervisor
#     # calculate progress
#     #