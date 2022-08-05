from pstats import Stats
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.serializers import SupersSerializer
from supers.models import Supers
from .models import SuperType
from .serializers import SupersTypeSerializer
from rest_framework import filters


# Create your views here.
# As a developer, I want to register the SuperType model with the admin site so I can:
# Register a new super user (python manage.py createsuperuser)
# Visit the admin site
# Seed two values (“Hero” and “Villain”) into the “super_type” table

# As a developer, I want to create a GET endpoint the responds with a 200 success status code and all 
# of the supers within the supers table.
# This view function should be implemented in a way to accept a “type” parameter
# Example: " http://127.0.0.1:8000/api/supers?type=hero”
# If a type query parameter is sent to the view function with the value of “hero”, 
# the view function response should be a list of all supers that are associated with the type of “Hero” 
# (Shown in End Result Overview video on portal)
# If a type query parameter is sent to the view function with the value of “villain”, 
# the view function response should be a list of all supers that are associated with the type of “Villain” 
# (Shown in End Result Overview video on portal)
# If no type query parameter is sent, return a custom dictionary response with a “heroes” key
# set equal to a list of supers of type “Hero” and a “villains” key set equal to a list of supers of type 
# “Villain” (Shown in End Result Overview video on portal)
# Custom_response = {“heroes” = [], “villains” = []}


@api_view (['GET'])

def super_type_list(request):

    super_type_param = request.query_params.get('type')
    primary_ability_param = request.query_params.get('primary_ability')
    super_types = SuperType.objects.all()

    class TypesView(GenericAPIView):
        queryset = Supers.objects.all()
        filter_backends = [filters.SearchFilter]
        search_fields = ['primary_ability']
   
    custom_response = {}

    if super_type_param:
        supers = Supers.objects.filter(super_type = super_type_param)
        serializer = SupersSerializer(supers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif primary_ability_param:
        supers = Supers.objects.filter(primary_ability = primary_ability_param)
        serializer = SupersSerializer(supers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        for super_type in super_types: # Custom_response = {“heroes” = [], “villains” = []}
            heroes = Supers.objects.filter(super_type_id = 1)
            hero_serializer = SupersSerializer(heroes, many = True)
            villains = Supers.objects.filter(super_type_id = 2)
            villain_serializer = SupersSerializer(villains, many = True)
            custom_response= {
            "Heroes": hero_serializer.data,
            "Villains": villain_serializer.data
        }

    return Response(custom_response, status=status.HTTP_200_OK)

