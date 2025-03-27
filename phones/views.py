from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Phones
from .serializers import PhonesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST',])
def phoneList(request,format=None):
    # Get all the phones
    if request.method=='GET':
        phones = Phones.objects.all()
        serializer = PhonesSerializer(phones, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=PhonesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def phoneDetail(request,id,format=None):
    try:
        phones=Phones.objects.get(pk=id)
    except Phones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serialzer=PhonesSerializer(phones)
        return Response(serialzer.data)
    elif request.method=='PUT':
        serialzer=PhonesSerializer(phones,data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        phones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)