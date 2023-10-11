from offer.models import Offer, RFQ
from rest_framework import viewsets, permissions
from .serializers import OfferSerializers, RFQSerializers


class OfferViewSet(viewsets.ModelViewSet):
    

    queryset = Offer.objects.all().order_by('-created_date')
    serializer_class = OfferSerializers




class RFQViewSet(viewsets.ModelViewSet):
    
    queryset = RFQ.objects.all().order_by('-created_date')
    serializer_class = RFQSerializers
