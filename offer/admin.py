from django.contrib import admin

from .models import Part, Customer, RFQ, Offer, OfferDetail

class OfferDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'offer']

class RFQAdmin(admin.ModelAdmin):
    list_display = ['id','srv_rfq_no','rfq_no', 'request_date', 'customer', 'part_quantity']


class PartAdmin(admin.ModelAdmin):
    list_display = ['part_no', 'name','customer']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['id','offer_no','rfq', 'related_person', 'status' ]
    exclude = ['offer_no', 'created_date']

admin.site.register(Part, PartAdmin)
admin.site.register(Customer)
admin.site.register(RFQ, RFQAdmin)
admin.site.register(Offer ,OfferAdmin)
admin.site.register(OfferDetail, OfferDetailAdmin)