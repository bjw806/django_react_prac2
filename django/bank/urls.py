from .views import Trasfer, EditAmount, ViewAmount, ViewAccounts, \
    ViewTransactions, EditTransactions, CreateTransactions, ViewTransactionDetail, ViewAccountDetail, SearchTransaction, \
    SearchTransactionPOST
from django.urls import path

app_name = 'bank'

urlpatterns = [
    path('', ViewAccounts.as_view(), name='listAccount'),
    path('user/', ViewAccounts.as_view(), name='viewAccounts'),
    path('user/<int:pk>/', ViewAccountDetail.as_view(), name='viewAccountDetail'),
    #path('user/<int:pk>/amount/', ViewAmount.as_view(), name='viewAmount'),
    path('user/amount/<int:pk>/', ViewAmount.as_view(), name='viewAmount'),
    path('user/edit/amount/<int:pk>/', EditAmount.as_view(), name='editAmount'),#

    path('transaction/transfer/', Trasfer.as_view(), name='transfer'),
    path('transaction/create/', CreateTransactions.as_view(), name='createTransaction'),
    path('transaction/edit/<int:pk>/', EditTransactions.as_view(), name='editTransaction'),
    path('transaction/view/', ViewTransactions.as_view(), name='viewTransactions'),
    path('transaction/view/<int:pk>/', ViewTransactionDetail.as_view(), name='viewTransactionDetail'),
    path('transaction/search/', SearchTransaction.as_view(), name='searchTransaction'),
    path('transaction/search/<int:pk>/', SearchTransactionPOST.as_view(), name='searchTransactionPOST'),
]

"""
송금 -> 잔액 조회 -> 잔액 수정
잔액 조회

!사용자 조회
!송금 기록 조회
!송금 기록 생성


"""