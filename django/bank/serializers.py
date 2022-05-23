from rest_framework import serializers
from users.models import TransferReport

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferReport
        fields = ('id', 'send_account', 'receive_account', 'amount')
