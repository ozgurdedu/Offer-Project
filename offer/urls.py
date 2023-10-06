from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.home_view, name = "offer-home"),
    path("create-offer", views.create_offer_view, name = "create-offer"),
    path("create-offer/<int:id>", views.create_offer_rfq_view, name = "create-offer-rfq"),
    path("user-offer/<int:id>", views.get_offer_byId, name = "user-offer"),
    path("update-offer/<int:id>", views.update_offer_view, name = "update-offer"),
    path("delete-offer/<int:id>", views.delete_offer_view, name = "delete-offer"),
    path("update-offer-status/<int:id>", views.update_offer_status, name = "update-offer-status"),
    path("offer-detail/<int:id>", views.offer_detail_view, name = "offer-detail"),
    path("get-detail/<int:id>", views.get_offer_detail_view, name = "get-offer-detail"),
    path("create-offer-detail", views.create_offer_detail_view, name = "create-offer-detail"),
    path("create-rfq", views.create_rfq_view, name = "create-rfq"),
    path("delete-rfq/<int:id>", views.delete_rfq_view, name = "delete-rfq"),
    path("rfqs", views.rfq_view, name = "rfqs"),
    path("confirm-rfq/<int:id>", views.confirm_rfq_view, name = "confirm-rfq"),
    path("customers", views.customers_view, name = "customers"),
    path("create-customer", views.create_customer_view, name = "create-customer"),
    path("delete-customer/<int:id>", views.delete_customer_view, name = "delete-customer"),
    path("update-customer/<int:id>", views.update_customer_view, name = "update-customer"),
    path("parts", views.parts_view, name = "parts"),
    path("create-part/<int:id>", views.create_part_customer_view, name = "create-part-customer"),
    path("create-part", views.create_part_view, name = "create-part"),
    path("update-part/<int:id>", views.update_part_view, name = "update-part"),
    path("delete-part/<int:id>", views.delete_part_view, name = "delete-part"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)