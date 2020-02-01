from django.shortcuts import render
from snippet_test.models import Snippet
from snippet_test.serializers import SnippetSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User


# Generic Class Based views
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)


# Generic Class Based views
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer