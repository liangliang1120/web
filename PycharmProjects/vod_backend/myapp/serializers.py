from rest_framework import serializers
from .models import MyModel, Video

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    class Meta:
        model = Video
        fields = '__all__'
