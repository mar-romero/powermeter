from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from powermeter_api.models import Mediciones
from powermeter_api.serializer import MedicionesSerializer
from django.http import JsonResponse
# Create your views here.


@api_view(['GET'])
def mediciones_list(request):
    mediciones = Mediciones.objects.all()
    serializer = MedicionesSerializer(mediciones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def mediciones_create(request):
    create_mediciones = request.data['mediciones']
    for c in create_mediciones:
        json_mediciones = {"mediciones": c}
        serializer = MedicionesSerializer(data=json_mediciones)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data)
        else:
            return Response(serializer.errors)
    return (Response(serializer.data))


@api_view(['GET'])
def mediciones_max(request):
    mediciones = Mediciones.objects.all()
    mediciones_python = list(mediciones.values())
    max_value = None
    for num in mediciones_python:
        num = int(num['mediciones'])
        if (max_value is None or num > max_value):
            max_value = num
            json_mediciones = {"mediciones": max_value}
    serializer = MedicionesSerializer(data=json_mediciones)
    if serializer.is_valid():
        serializer.save()
        return (Response(serializer.data))
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def mediciones_min(request):
    mediciones = Mediciones.objects.all()
    mediciones_python = list(mediciones.values())
    min_value = None
    for num in mediciones_python:
        num = int(num['mediciones'])
        if (min_value is None or num < min_value):
            min_value = num
            json_mediciones = {"mediciones": min_value}
    serializer = MedicionesSerializer(data=json_mediciones)
    if serializer.is_valid():
        serializer.save()
        return (Response(serializer.data))
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def mediciones_averge(request):
    mediciones = Mediciones.objects.all()
    mediciones_python = list(mediciones.values())
    total = len(mediciones_python)
    max_value = 0
    for num in mediciones_python:
        num = int(num['mediciones'])
        max_value += num
    avg_value = max_value/total
    json_mediciones = {"mediciones": avg_value}
    serializer = MedicionesSerializer(data=json_mediciones)
    if serializer.is_valid():
        serializer.save()
        return (Response(serializer.data))
    else:
        return Response(serializer.errors)

@api_view(['GET','DELETE'])
def mediociones_delete(request,pk):
    mediciones = Mediciones.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = MedicionesSerializer(mediciones)
        return Response(serializer.data)
    if request.method == 'DELETE':
        mediciones.delete()
        return Response({
            'delete':True
            }
        )