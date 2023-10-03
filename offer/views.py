from django.shortcuts import render, redirect
from .models import Offer, RFQ, Customer, Part
from .forms import CreateOfferForm, CreateRFQForm, CreateCustomerForm, CreateOfferRFQForm, CreatePartForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone

def home_view(request):
    offers = Offer.objects.order_by('-created_date')
    offer_count = offers.count()
    context = {'offers':offers, 'offer_count':offer_count}
    return render(request, 'offer/home.html',context)

# @@@@@@@@@@@@@@@@@ OFFER

@login_required(login_url='/user/login')
def get_offer_byId(request, id):
    offers = Offer.objects.filter(related_person__id=id).order_by('-created_date')
    offer_count = offers.count()
    context = {'offers':offers, 'offer_count':offer_count}
    return render(request, 'offer/offer-detail.html', context)

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
            return redirect('offer-detail', id=request.user.id)

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
     
     print(rfq)
     if request.method == "POST":
          form = CreateOfferRFQForm(request.POST, initial=initial)
          if form.is_valid():
              offer = form.save(commit=False)
              offer.related_person = request.user
              form.save()
              return redirect('offer-detail', id=request.user.id)
        
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
            return redirect('offer-detail', id=request.user.id)

    else:
        form = CreateOfferForm(instance=offer)

    context = {'form':form, 'offer':offer}
    return render(request, 'offer/update-offer.html', context)

@login_required(login_url='/user/login')
def delete_offer_view(request, id):
    try:
        offer = get_object_or_404(Offer, id=id)
        offer.delete()
        return redirect('offer-detail', id = request.user.id)
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

    if request.method == "POST":
        form = CreateRFQForm(request.POST, initial={'request_date':timezone.now})
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.status = "uygun" if request.user.is_staff else "inceleniyor"
            form.save()
            return redirect('rfqs')
    else:
        form = CreateRFQForm(initial={'request_date':timezone.now})
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

