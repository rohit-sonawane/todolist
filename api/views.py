# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .serializers import TodoListSerializer
from .models import TodoList

from rest_framework import permissions
from .permissions import IsOwner  

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    
    #queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
      
    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user) 
