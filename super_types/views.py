from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.serializers import SupersSerializer
from supers.models import Supers
from .models import SuperType
from .serializers import 


# Create your views here.

@api_view (['GET'])
def super_type_list(request):

    super_types = SuperType.objects.all()

    custom_response_dictionary = {}

    for super_type in super_types:
        supers = Supers.objects.filter(super_type_id = super_type.id)
        supers_serializer = SupersSerializer(supers, many = True)

        custom_response_dictionary[super_type.type] = {
            "type": super_type.type,
            "supers": supers_serializer.data
        }

    return Response(custom_response_dictionary)

