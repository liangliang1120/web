from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from .models import MyModel, Video
from .serializers import MyModelSerializer, VideoSerializer
import uuid
from rest_framework.response import Response

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer




class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # def create(self, request, *args, **kwargs):
    #     # Set the uuid field to a new UUID value
    #     request.data["uuid"] = str(uuid.uuid4())
    #
    #     # Create a new serializer with the modified data
    #     serializer = self.get_serializer(data=request.data)
    #
    #     # Validate the serializer and save the new object
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     # Return a response with the serialized data and a 201 status code
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
