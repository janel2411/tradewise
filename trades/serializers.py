from rest_framework import serializers
from .models import TradingSession

class TradingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingSession
        fields = '__all__'
