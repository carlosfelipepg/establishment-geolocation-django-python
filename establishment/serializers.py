from rest_framework import serializers
from establishment.models import Establishment


class EstablishmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Establishment
        fields = '__all__'
