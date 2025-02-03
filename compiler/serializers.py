from rest_framework import serializers
from .models import CodeHistory

class CodeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeHistory
        fields = ['id', 'code', 'output', 'timestamp']
