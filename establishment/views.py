from rest_framework import viewsets, exceptions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from establishment.models import Establishment
from establishment.serializers import EstablishmentSerializer

from math import radians, sin, cos, asin, sqrt


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (AllowAny,)

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        return 2 * 6371 * asin(sqrt(a))

    @action(methods=["post"], detail=False, permission_classes=[AllowAny, ])
    def order_establishment_by_distance(self, request):
        lat = request.data['lat']
        lon = request.data['lon']
        if not lat or not lon:
            return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)

        establishment_list = Establishment.objects.values()
        data = [{'name': x['name'], 'distance': self.haversine(lat, lon, x['latitude'], x['longitude'])}
                for x in
                establishment_list]
        data.sort(key=lambda x: x['distance'])
        return Response(data)
