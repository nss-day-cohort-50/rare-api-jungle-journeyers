from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareapi.models import Categories


class CatView(ViewSet):
        """Categories"""
def retrieve(self, request, pk=None):
    """Handle GET requests for single cat type

    Returns:
        Response -- JSON serialized cat type
    """
    try:
        cat = Categories.objects.get(pk=pk)
        serializer = CatSerializer(cat, context={'request': request})
        return Response(serializer.data)
    except Exception as ex:
        return HttpResponseServerError(ex)
def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized cat instance
        """

        # Uses the token passed in the `Authorization` header
        cat = Categories.objects.get(user=request.auth.user)

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `CatId` in the body of the request.
        #game = Cat.objects.get(pk=request.data["CatId"])
        #Add Attendee after the table is created.

        # Try to save the new cat to the database, then
        # serialize the cat instance as JSON, and send the
        # JSON as a response to the client request
        try:
            # Create a new Python instance of the Cat class
            # and set its properties from what was sent in the
            # body of the request from the client.
            cat = Categories.objects.create(
                game_id=request.data["game_id"],
                description=request.data["description"],
                date=request.data["date"],
                time=request.data["time"],
                organizer=cat
            )
            serializer = CatSerializer(cat, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
class CatSerializer(serializers.ModelSerializer):
     class Meta:
        model = Categories()
        fields = ['label']