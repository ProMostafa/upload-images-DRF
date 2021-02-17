from django.shortcuts import render
from .models import Pictures
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class upload_images(APIView):
    def get(self, request):
        images = Pictures.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        # converts querydict to original dict
        images = dict((request.data).lists())['picture']
        print(images)
        for image in images:
            print(image)
            serializer = ImageSerializer(data={'picture': image})
            if serializer.is_valid():
                 Pictures.objects.create(picture=image)
            else:
                 return Response({'error': 'Failed to load images'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Images uploaded successfully'}, status=status.HTTP_200_OK)




