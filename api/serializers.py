from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        # 公開したい項目
        fields = ['id','title', 'img']