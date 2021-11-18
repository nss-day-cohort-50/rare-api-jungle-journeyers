from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rareapi.models import RareUser, Posts, Comments

class CommentView(ViewSet):
    def create(self, request):
        rare_user = RareUser.objects.get(user=request.auth.user)
        post = Posts.objects.get(pk=request.data['post'])
        
        try:
            comment = Comments.objects.create(
               content=request.data["content"],
               created_on = request.data['created_on'],
               post = post,
               author = rare_user
            )
            
            serializer = CommentSerializer(comment, context={'request': request})
            return Response("sure")
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        comments = Comments.objects.get(pk=pk)
        serializer = CommentSerializer(comments, context={'request': request})
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        try:
            comments = Comments.objects.get(pk=pk)
            comments.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comments.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
        
class RareSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        
        model = RareUser
        fields = ('user',)
        
class CommentSerializer(serializers.ModelSerializer):
    author = RareSerializer()
    
    class Meta:
        model = Comments
        fields = ('id', 'content', 'created_on', 'post', 'author')
        depth = 1
            
