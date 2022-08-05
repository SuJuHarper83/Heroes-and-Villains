from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.serializers import SupersSerializer
from supers.models import Supers
from .models import SuperType
from .serializers import SupersTypeSerializer


# Create your views here.

@api_view (['GET'])
def super_type_list(request):

    super_type_param = request.query_params.get('type')
    primary_ability_param = request.query_params.get('primary_ability')
    super_types = SuperType.objects.all()
    super_types = SuperType.objects.all()
   
    custom_response = {}

    if super_type_param:
        supers = Supers.objects.filter(super_type = super_type_param)
        serializer = SupersSerializer(supers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif primary_ability_param:
        supers = Supers.objects.filter(primary_ability = primary_ability_param)
        serializer = SupersSerializer(supers, many = True)
    else:
        for super_type in super_types:
            heroes = Supers.objects.filter(super_type_id = 1)
            hero_serializer = SupersSerializer(heroes, many = True)
            villains = Supers.objects.filter(super_type_id = 2)
            villain_serializer = SupersSerializer(villains, many = True)
            custom_response= {
            "Heroes": hero_serializer.data,
            "Villains": villain_serializer.data
        }

    return Response(custom_response, status=status.HTTP_200_OK)

