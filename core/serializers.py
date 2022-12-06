from rest_framework import serializers
from .models import core
class GetTraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = core
        fields = ('id', 'SSN','lastname','firstname','birthday','phone','address','company')  

class CoreSerializer(serializers.Serializer):
    SSN = serializers.IntegerField()
    lastname = serializers.CharField(max_length = 255)
    firstname = serializers.CharField(max_length = 255)
    birthday = serializers.DateField()
    phone = serializers.IntegerField(default=0)
    address = serializers.CharField()
    company = serializers.CharField()