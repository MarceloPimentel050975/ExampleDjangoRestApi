from rest_framework import serializers
from endereco.models import Endereco



class EnderecoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    streetName=serializers.CharField(max_length=200, required=True)
    number=serializers.CharField(max_length=10, required=True)
    complement=serializers.CharField(max_length=500, required=True)
    neighbourhood=serializers.CharField(max_length=300, required=True)
    city=serializers.CharField(max_length=300, required=True)
    state=serializers.CharField(max_length=200, required=True)
    country=serializers.CharField(max_length=200, required=True)
    zipcode=serializers.CharField(max_length=15, required=True)
    latitude=serializers.CharField(max_length=30, required=False)
    longitude=serializers.CharField(max_length=30, required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Endereco.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.streetName = validated_data.get('streetName', instance.streetName)
        instance.number = validated_data.get('number', instance.streetName)
        instance.complement = validated_data.get('complement', instance.streetName)
        instance.neighbourhood = validated_data.get('neighbourhood', instance.streetName)
        instance.city = validated_data.get('city', instance.streetName)
        instance.state = validated_data.get('state', instance.streetName)
        instance.country = validated_data.get('country', instance.streetName)
        instance.zipcode = validated_data.get('zipcode', instance.streetName)
        instance.latitude = validated_data.get('latitude', instance.streetName)
        instance.longitude = validated_data.get('longitude', instance.streetName)
        instance.save()
        return instance