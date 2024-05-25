from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Snippet.objects.add()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
