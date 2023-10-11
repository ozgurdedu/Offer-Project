from offer.models import Offer, RFQ, Part, Customer
from rest_framework import serializers
from django.contrib.auth.models import User


# class PartSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Part
#         fields = '__all__'


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name']




class PartSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ['name','part_no', 'unit_price','mold_price']


class CustomerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'country', 'industry']





class RFQSerializers(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializers()
    class Meta:
        model = RFQ
        fields = ['id','rfq_no', 'srv_rfq_no', 'customer']



class OfferSerializers(serializers.HyperlinkedModelSerializer):
    #part  = PartSerializers()
    #related_person = UserSerializers()
    part = PartSerializers()
    rfq = RFQSerializers()
    class Meta:
        model = Offer
        fields = ['id','offer_no', 'created_date', 'status', 'rfq', 'part']
    
