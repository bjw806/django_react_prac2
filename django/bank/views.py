from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, generics, filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from users.serializers import CustomUserSerializer, EditUserSerializer
from .serializers import TransferSerializer
from users.models import NewUser, TransferReport
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from rest_framework.generics import get_object_or_404
import json

class Trasfer(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #parser_classes = [MultiPartParser, FormParser]
    parser_classes = [JSONParser]

    def create(self, request, format=None):
        received_json_data = json.loads(request.body.decode("utf-8"))

        serializer = TransferSerializer(data=request.data)
        #send_account = request.data['send_account']
        #receive_account = request.data['receive_account']
        #amount = int(request.data['amount'])

        print(received_json_data)
        send_account = received_json_data['send_account']
        receive_account = received_json_data['receive_account']
        amount = int(received_json_data['amount'])

        print(send_account,receive_account,amount)

        if amount < 0:
            return Response("양의 값을 입력하세요.", status=status.HTTP_200_OK)

        my_account = NewUser.objects.get(account_address=send_account)

        response = {
            'done': True,
            'error': ''
        }

        try:
            send_account = NewUser.objects.select_for_update().get(account_address=send_account)
            receive_account = NewUser.objects.select_for_update().get(account_address=receive_account)
        except:
            print('error')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            if amount > my_account.account_money:
                response['done'] = False
                response['error'] = 'rejected'
                return HttpResponse(json.dumps(response), 'application/javascript; charset=utf8')
            else:

                send_account.account_money -= amount
                receive_account.account_money += amount
                send_account.save()
                receive_account.save()
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#OK
class EditAmount(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EditUserSerializer
    queryset = NewUser.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data["account_money"], status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewAmount(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()
    def viewAmount(self, request, *args, **kwargs):
        item = self.kwargs.get('pk')
        data = get_object_or_404(NewUser, account_address=item)
        print(data)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=data, partial=True)
        print(serializer)
        if serializer.is_valid():
            return Response(serializer.data["account_money"], status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #def get_object(self, queryset=None, **kwargs):
    #    item = self.kwargs.get('pk')
    #    from rest_framework.generics import get_object_or_404
    #    return get_object_or_404(NewUser, id=item)
#OK
class ViewAccounts(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

#OK
class ViewAccountDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        from rest_framework.generics import get_object_or_404
        return get_object_or_404(NewUser, account_address=item)

#OK
class ViewTransactions(generics.ListAPIView):
    serializer_class = TransferSerializer
    queryset = TransferReport.objects.all()

#OK
class ViewTransactionDetail(generics.RetrieveAPIView):
    serializer_class = TransferSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        from rest_framework.generics import get_object_or_404
        return get_object_or_404(TransferReport, id=item)

#OK
class EditTransactions(generics.UpdateAPIView):
    serializer_class = TransferSerializer
    queryset = TransferReport.objects.all()

#OK
class CreateTransactions(generics.CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    def create(self, request, format=None):
        print(request.data)
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchTransaction(generics.ListAPIView):
    queryset = TransferReport.objects.all()
    serializer_class = TransferSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^account_address']  # ^, =

class SearchTransactionPOST(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(NewUser, account_address=item)

""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""