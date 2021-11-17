"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework import response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Posts, RareUser, Categories

class PostView(ViewSet):
    def create(self, request):
        
        user = RareUser.objects.get(user=request.auth.user)
        category = Categories.objects.get(pk=request.data["categoryId"])
        
        try:
            post = Posts.objects.create(
                user = user,
                category = category,
                title = request.data['title'],
                publication_date = request.data['publicationDate'],
                content = request.data['content'],
                approved = request.data['approved']
            )
            serializer = PostSerializer(post, context = {'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            post = Posts.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')
        
class RareUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = RareUser
        fields = ('user', )
  

class PostSerializer(serializers.ModelSerializer):
    user = RareUserSerializer()
    class Meta:
        model = Posts
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'content', 'approved')
        depth = 1
        
        