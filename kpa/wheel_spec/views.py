from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

class WheelSpecCreateView(APIView):
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WheelSpecListView(APIView):
    def get(self, request):
        specs = WheelSpecification.objects.all()
        serializer = WheelSpecificationSerializer(specs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
