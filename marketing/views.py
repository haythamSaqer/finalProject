from django.http import Http404
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MarketingMeeting, MeetingType, Contract
from .permissions import ContractApprovePermission
from .serializers import MeetingTypeSerializer, ContractSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class MeetingList(generics.ListCreateAPIView):
    queryset = MarketingMeeting.objects.all()
    serializer_class = ContractSerializer
    pagination_class = StandardResultsSetPagination


class MeetingTypeList(generics.ListCreateAPIView):
    queryset = MeetingType.objects.all()
    serializer_class = MeetingTypeSerializer


class MeetingTypeDD(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return MeetingType.objects.get(pk=pk)
        except MeetingType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = MeetingTypeSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = MeetingTypeSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'options'])
@permission_classes([ContractApprovePermission])
@authentication_classes([TokenAuthentication])
def approve_contract(request, pk):
    try:
        contract = Contract.objects.get(id=pk)
        contract.adminApproval = True
        contract.save()
        return Response({'status': 'Approved successfully !'}, status=status.HTTP_200_OK)
    except Contract.DoesNotExist:
        return Response({'status':'Object not exists !'}, status=status.HTTP_403_FORBIDDEN)