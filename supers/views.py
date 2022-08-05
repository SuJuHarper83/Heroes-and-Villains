from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Supers
from super_types.models import SuperType
from .serializers import SupersSerializer

# Create your views here.
# As a developer, I want to create a GET by id endpoint that does the following things:
# Accepts a value from the request’s URL (The id of the super to retrieve).
# Returns a 200 status code.
# Responds with the super in the database that has the id that was sent through the URL.

# As a developer, I want to create a POST endpoint that does the following things:
# Accepts a body object from the request in the form of a Super model.
# Adds the new super to the database.
# Returns a 201 status code.
# Responds with the newly created super object.

@api_view(['GET', 'POST'])
def supers_list(request):
    supers_list_param = request.query_params.get('supers_list')
    
    if request.method == "GET":
        
        print(supers_list_param)

        supers = Supers.objects.all()

    if supers_list_param:
        supers = supers.filter(supers_list__name = supers_list_param)

    elif request.method == "POST":
        serializer = SupersSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    serializer = SupersSerializer(supers, many=True)

    return Response(serializer.data)

# As a developer, I want to create a PUT endpoint that does the following things:
# Accepts a value from the request’s URL (The id of the super to be updated).
# Accepts a body object from the request in the form of a Super model.
# Finds the super in the Super table and updates that super with the properties that were sent in the request’s body.
# Returns a 200 status code.
# Responds with the newly updated super object.

# As a developer, I want to create a DELETE endpoint that does the following things:
# Accepts a value from the request’s URL.
# Deletes the correct super from the database
# Returns a 204 status code (NO CONTENT).

@api_view (['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk = pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers);
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

