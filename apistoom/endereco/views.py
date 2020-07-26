# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer

@csrf_exempt
def endereco_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EnderecoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@csrf_exempt
def endereco_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        endereco = Endereco.objects.get(pk=pk)
    except Enderecot.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EnderecoSerializer(endereco)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EnderecoSerializer(endereco, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        endereco.delete()
        return HttpResponse(status=204)