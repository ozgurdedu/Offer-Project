from django.shortcuts import render, redirect
from .models import Offer, RFQ, Customer, Part, OfferDetail
from .forms import CreateOfferForm, CreateRFQForm, CreateCustomerForm, CreateOfferRFQForm, CreatePartForm, CreateOfferDetailForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
import pandas as pd
import os
from django.http import HttpResponse
import tempfile
from django.db.models import Q 


def home_view(request):

    search_post = request.GET.get('search')
    if search_post:
        offers = Offer.objects.filter(
            Q(offer_no__icontains=search_post)| 
            Q(date__icontains=search_post) | 
            Q(rfq__rfq_no__icontains=search_post) | 
            Q(rfq__srv_rfq_no__icontains=search_post) | 
            Q(part__part_no__icontains=search_post) |
            Q(part__name__icontains=search_post) | 
            Q(status__icontains=search_post) |
            Q(related_person__first_name__icontains=search_post) |
            Q(related_person__last_name__icontains=search_post) | 
            Q(rfq__customer__name__icontains=search_post)
        )
    else:
        offers = Offer.objects.order_by('-created_date')

    offer_count = offers.count()
    context = {'offers':offers,
                'offer_count':offer_count}
    
    return render(request, 'offer/home.html',context)

# @@@@@@@@@@@@@@@@@ OFFER

@login_required(login_url='/user/login')
def get_offer_byId(request, id):
    offers = Offer.objects.filter(related_person__id=id).order_by('-created_date')
    offer_count = offers.count()
    context = {'offers':offers, 'offer_count':offer_count}
    return render(request, 'offer/user-offer.html', context)

@login_required(login_url='/user/login')
def create_offer_view(request):

    initial = { 
         'date' : timezone.now,
         'status' : 'inceleniyor'
     }

    if request.method == "POST":
        form = CreateOfferForm(request.POST, initial=initial)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.related_person = request.user
            form.save()
            return redirect('user-offer', id=request.user.id)

    else:
        form = CreateOfferForm(initial=initial)
    context = {'form':form}
    return render(request, 'offer/create-offer.html', context)

@login_required(login_url='/user/login')
def create_offer_rfq_view(request, id):
     rfq = get_object_or_404(RFQ, id=id)
     
     initial = {
         'rfq' : rfq, 
         'date' : timezone.now,
         'status' : 'inceleniyor'
     }
     
     if request.method == "POST":
          form = CreateOfferRFQForm(request.POST, initial=initial)
          if form.is_valid():
              offer = form.save(commit=False)
              offer.related_person = request.user
              form.save()
              return redirect('user-offer', id=request.user.id)
        
     else:
          form = CreateOfferRFQForm(initial=initial)
     context = {"form":form, "rfq":rfq}
     return render(request, 'offer/create-offer-rfq.html', context)


@login_required(login_url='/user/login')
def update_offer_view(request, id):
    offer = Offer.objects.get(id=id)
    if request.method == "POST":
        form = CreateOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('user-offer', id=request.user.id)

    else:
        form = CreateOfferForm(instance=offer)

    context = {'form':form, 'offer':offer}
    return render(request, 'offer/update-offer.html', context)

@login_required(login_url='/user/login')
def delete_offer_view(request, id):
    try:
        offer = get_object_or_404(Offer, id=id)
        offer.delete()
        return redirect('user-offer', id = request.user.id)
    except Offer.DoesNotExist:
        return redirect('offer-home')

@login_required(login_url='/user/login')
def update_offer_status(request, id):
    offer = Offer.objects.get(id=id)
  
    if offer.status == "inceleniyor":
        offer.status = "gonderildi"
        offer.save()
    elif offer.status == "gonderildi":
        offer.status = "inceleniyor"
        offer.save()
  
    return redirect('offer-home')
# from django.http import JsonResponse
# @login_required(login_url='/user/login')
# def update_offer_status(request, id):
#     offer = Offer.objects.get(id=id)
    
#     if request.method == 'POST':
#         new_status = request.POST.get('new_status')
        
#         if new_status == 'inceleniyor':
#             offer.status = 'inceleniyor'
#         elif new_status == 'gonderildi':
#             offer.status = 'gonderildi'
        
#         offer.save()
        
#         return JsonResponse({'success': True})
    
#     return JsonResponse({'success': False})

# from django.http import JsonResponse

# @login_required(login_url='/user/login')
# def update_offer_status(request, id):
#     offer = Offer.objects.get(id=id)
    
#     if request.method == 'POST':
#         new_status = request.POST.get('new_status')
        
#         if new_status == 'inceleniyor':
#             offer.status = 'inceleniyor'
#         elif new_status == 'gonderildi':
#             offer.status = 'gonderildi'
        
#         offer.save()
        
#         return JsonResponse({'success': True, 'new_status': offer.status})
    
#     return JsonResponse({'success': False})









# @@@@@@@@@@@@@@@@@ RFQ

# def is_admin(user):
#     return user.is_staff

# @user_passes_test(is_admin)
def rfq_view(request):
    rfqs = RFQ.objects.order_by('-created_date')

    rfq_count = rfqs.count()
    context = {'rfqs':rfqs, 'rfq_count':rfq_count}
    return render(request, 'offer/rfqs.html', context)


@login_required(login_url='/user/login')
def create_rfq_view(request):
    initial = {
         'request_date' : timezone.now,
         'status' : 'in progress'
     }
     
    if request.method == "POST":
        form = CreateRFQForm(request.POST, initial=initial)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.status = "uygun" if request.user.is_staff else "inceleniyor"
            form.save()
            return redirect('rfqs')
    else:
        form = CreateRFQForm(initial=initial)
    context = {'form':form}
    return render(request, 'offer/create-rfq.html', context)

@login_required(login_url='/user/login')
def delete_rfq_view(request, id):
    try:
        rfq = get_object_or_404(RFQ,id=id)
        rfq.delete()
        return redirect('rfqs')

    except RFQ.DoesNotExist:
        return redirect('rfqs') 


@login_required(login_url='/user/login')
def confirm_rfq_view(request, id):
    
    rfq = RFQ.objects.get(id=id)
    rfq.status = "uygun"
    rfq.save()
    return redirect('rfqs')




# @@@@@@@@@@@@@@@@@ CUSTOMER

def customers_view(request):
    search_post = request.GET.get('search')
    if search_post:
        customers = Customer.objects.filter(
            Q(name__icontains=search_post)
        )
    else:
        customers = Customer.objects.order_by('-created_date')
    context = {'customers':customers}
    return render(request, 'offer/customers.html', context)

# @login_required(login_url='/user/login')
def create_customer_view(request):
    if request.method == "POST":
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CreateCustomerForm()
    context = {'form':form}
    return render(request, 'offer/create-customer.html', context)

@login_required(login_url='/user/login')
def update_customer_view(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CreateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CreateCustomerForm(instance=customer)

    context = {'form':form}
    return render(request, 'offer/update-customer.html', context)

@login_required(login_url='/user/login')
def delete_customer_view(request, id):
    try:
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
        return redirect('customers')
    except Customer.DoesNotExist:
        return redirect('customers')


# @@@@@@@@@@@@@@@@@ PART

def parts_view(request):
    search_post = request.GET.get('search')
    if search_post:
        parts = Part.objects.filter(
            Q(name__icontains=search_post) | 
            Q(customer__name__icontains=search_post) 
        )
    else:
        parts = Part.objects.order_by('-created_date')
    context = {'parts':parts}
    return render(request, 'offer/parts.html',context)



@login_required(login_url='/user/login')
def create_part_customer_view(request, id):
    customer = get_object_or_404(Customer, id=id)
    
    initial = {'customer':customer}

    if request.method == "POST":
        form = CreatePartForm(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            return redirect('parts')
    else:
        form = CreatePartForm(initial=initial)

    context = {'form':form}
    return render(request, 'offer/create-part.html', context)


def create_part_view(request):
    if request.method == "POST":
        form = CreatePartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parts')
    else:
        form = CreatePartForm()
    context = {'form':form}
    return render(request, 'offer/create-part.html',context)
def update_part_view(request,id):
    part = get_object_or_404(Part, id=id)
    if request.method == "POST":
        form = CreatePartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('parts')
    else:
        form = CreatePartForm(instance=part)
    context = {'form':form}
    return render(request, 'offer/update-part.html',context)   
    
def delete_part_view(request,id):
    try:
        part = get_object_or_404(Part, id=id)
        part.delete()
        return redirect('parts')
    except Part.DoesNotExist:
        return redirect('parts')

# @@@@@@@@@@@@@@@@@ OFFER DETAIL

@login_required(login_url='/user/login')
def offer_detail_view(request, id):
   
    offer = get_object_or_404(Offer, id=id)
    try:
        offer_detail = OfferDetail.objects.get(offer=offer)
    except OfferDetail.DoesNotExist:
        return redirect('offer-home')
    
    context = {'offer_detail':offer_detail}
    return render(request, 'offer/offer-detail.html', context)


@login_required(login_url='/user/login')
def get_offer_detail_view(request, id):

    offer_detail = get_object_or_404(OfferDetail, id=id)

    d = {'#' : [offer_detail.offer.rfq.customer,
                offer_detail.offer.part.part_no,
                offer_detail.offer.part.name, 
                offer_detail.malzeme, 
                offer_detail.dokum_tipi,
                offer_detail.maca_tipi,
                offer_detail.parca_agirligi_kg,
                offer_detail.maca_agirligi_kg,
                offer_detail.yillik_adet, 
                offer_detail.min_siparis_adedi, 
                offer_detail.para_birimi,
                offer_detail.parca_fiyati,
                offer_detail.kalip_fiyati,
                offer_detail.teslim_turu,
                offer_detail.kalip_goz_sayisi,
                offer_detail.maca_goz_sayisi,
                offer_detail.kalip_omru_baski_sayisi,
                offer_detail.kum_dokum,
                offer_detail.kokil_dokum,
                offer_detail.enjeksiyon_dokum,
                offer_detail.sicak_maca,
                offer_detail.soguk_maca,
                offer_detail.takalama,
                offer_detail.testere,
                offer_detail.zimpara,
                offer_detail.tesviye,
                offer_detail.kumlama,
                offer_detail.test_sizdirmazlik,
                offer_detail.test_temizleme,
                offer_detail.isil_islem_kg,
                offer_detail.isil_islem_sarj,
                offer_detail.vibrasyon,
                offer_detail.cnc_dik_isleme,
                offer_detail.cnc_yatay_isleme,
                offer_detail.torna,
                offer_detail.heli_coil,
                offer_detail.montaj_parca,
                offer_detail.montaj_kaynak,
                offer_detail.paketleme,
                offer_detail.emprenye,
                offer_detail.kaplama,
                offer_detail.boya,
                offer_detail.dis_isleme,
                offer_detail.x_ray_testi,
                offer_detail.mukavemet_testi,
                offer_detail.nakliye_maliyeti,
                

                ]
    }
    df = pd.DataFrame(data=d, index = [
        "Customer",
        "Part No",
        "Part Name", 
        "Malzeme",
        "Döküm Tipi",
        "Maça Tipi",
        "Parça Ağırlığı (Kg)",
        "Maça Ağırlığı (Kg)",
        "Yıllık Adet",
        "Min Sipariş Adedi",
        "Para Birimi",
        "Parça Fiyatı",
        "Kalıp Fiyatı",
        "Teslim Türü",
        "Kalıp Göz Sayısı",
        "Maça Göz Sayısı",
        "Kalıp Ömrü Baskı Sayısı",
        "Kum Döküm",
        "Kokil Döküm", 
        "Enjeksiyon Döküm",
        "Sıcak Maça",
        "Soğuk Maça",
        "Takalama",
        "Testere",
        "Zımpara",
        "Tesviye",
        "Kumlama",
        "Test (Sızdırmazlık)",
        "Test (Temizleme)", 
        "Isıl İşlem (kg bazında hesaplama için)",
        "Isıl İşlem (şarf bazında hesaplama için)",
        "Vibrasyon", 
        "CNC (Dik İşleme)",
        "CNC Yatay İşleme",
        "Torna",
        "Heli-Coil",
        "Montaj (Parça)",
        "Montaj (Kaynak)",
        "Paketleme",
        "Emprenye",
        "Kaplama",
        "Boya",
        "Dış İşleme",
        "X-Ray Testi",
        "Mukavemet Testi",
        "Nakliye Maliyeti"
    ])


   
        # Excel dosyasını oluştur
    excel_file_path = "offer_detail.xlsx"
    df.to_excel(excel_file_path)
     # Excel dosyasını HttpResponse olarak döndür
    with open(excel_file_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read())
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response['Content-Disposition'] = f"attachment; filename={offer_detail.offer}_details.xlsx"
    return response

    # context = {'offer_detail':offer_detail, 'df1':df1, 'df2':df2}
    # return render(request, 'offer/offer-detail.html', context)


@login_required(login_url='/user/login')
def create_offer_detail_view(request, id):
    
    offer = get_object_or_404(Offer, id=id)
    
    if request.method == "POST":
        form = CreateOfferDetailForm(request.POST, initial={'offer':offer})
        if form.is_valid():
            form.save()
            return redirect('user-offer', id = request.user.id)
    else:
        form = CreateOfferDetailForm(initial={'offer':offer})
    
    
    context = {'form':form}

    return render(request, 'offer/create-offer-detail.html', context)


@login_required(login_url='/user/login')
def update_offer_detail_view(request, id):
    
    offer = get_object_or_404(Offer, id=id)
    offer_detail = OfferDetail.objects.get(offer=offer)
    if request.method == "POST":
        form = CreateOfferDetailForm(request.POST, instance=offer_detail)
        if form.is_valid():
            form.save()
            return redirect('user-offer', id = request.user.id)
    else:
        form = CreateOfferDetailForm(instance=offer_detail)
    
    
    context = {'form':form, 'offer_detail':offer_detail}

    return render(request, 'offer/update-offer-detail.html', context)



@login_required(login_url='/user/login')
def delete_offer_detail_view(request, id):
    offer_detail = get_object_or_404(OfferDetail, id=id)
    offer_detail.delete()
    return redirect('user-offer', id = request.user.id)