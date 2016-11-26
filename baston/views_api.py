from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import BastonSerializer
from .models import Baston

class BastonListado(APIView):
  def get(self, request, format=None):
    listado = Baston.objects.all()
    serializer = BastonSerializer(listado, many = True)
    return Response(serializer.data)

  def post(self, request, format=None):
    baston = BastonSerializer(data = request.data)

    if baston.is_valid():
      baston.save()
      return Response(baston.data,status=status.HTTP_201_CREATED)
    return Response(baston.data,status=status.HTTP_400_BAD_REQUEST)

class BastonDetalleView(APIView):
  def get(self, request, pk, format=None):
    baston = get_object_or_404(Baston,pk=pk)
    serialize = BastonSerializer(baston)
    return Response(serialize.data)
    
  def put(self, request, pk, format=None):
    baston = get_object_or_404(Baston, pk=pk)
    serializer = BastonSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    baston = get_object_or_404(Baston, pk=pk)
    baston.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
from rest_framework import generics
from .serializer import BastonSerializerV2

class BastonListadoV2(generics.ListCreateAPIView):
  queryset = Baston.objects.all()
  serializer_class = BastonSerializerV2


class BastonDetalleViewV2(generics.RetrieveUpdateDestroyAPIView):
  queryset = Baston.objects.all()
  serializer_class = BastonSerializerV2

from rest_framework import viewsets

class BastonViewSet(viewsets.ModelViewSet):
  queryset = Baston.objects.all()
  serializer_class = BastonSerializerV2
