from django.shortcuts import render
from rest_framework.views import APIView
from .models import Posts
from .serializer import PostsSerializer
from rest_framework import Response


class PostsView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "body": output.body,
                "author": output.author
            } for output in PostsSerializer(data=request.data)
        ]
        return Response(output)

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)