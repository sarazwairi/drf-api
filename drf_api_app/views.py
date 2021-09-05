from rest_framework import generics
# from django.shortcuts import render
from .serializers import PostSerializer
from .models import Things

# Create your views here.
class ThingsList(generics.ListCreateAPIView):
    queryset=Things.objects.all()
    serializer_class=PostSerializer

class ThingsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Things.objects.all()
    serializer_class=PostSerializer

