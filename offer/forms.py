from django import forms
from .models import Offer, RFQ, Part, Customer, OfferDetail
from django_countries.fields import CountryField
INDUSTRIES = (
    ('accounting', ('Accounting')),
    ('airlines', ('Airlines/Aviation')),
    ('alternativemedicine', ('Alternative Medicine')),
    ('analyticsdata', ('Analytics / Data Science')),
    ('animation', ('Animation')),
    ('apparel', ('Apparel/Fashion')),
    ('architecture', ('Architecture/Planning')),
    ('arts', ('Arts/Crafts')),
    ('automotive', ('Automotive')),
    ('aviation', ('Aviation/Aerospace')),
    ('banking', ('Banking/Mortgage')),
    ('biotechnology', ('Biotechnology/Greentech')),
    ('broadcastmedia', ('Broadcast Media')),
    ('buildingmaterials', ('Building Materials')),
    ('businesssupplies', ('Business Supplies/Equipment')),
    ('capitalmarkets', ('Capital Markets/Hedge Fund/Private Equity')),
    ('chemicals', ('Chemicals')),
    ('civic', ('Civic/Social Organization')),
    ('civilengineering', ('Civil Engineering')),
    ('commercialrealestate', ('Commercial Real Estate')),
    ('computergames', ('Computer Games')),
    ('computerhardware', ('Computer Hardware')),
    ('computernetworking', ('Computer Networking')),
    ('computersoftware', ('Computer Software/Engineering')),
    ('computer', ('Computer/Network Security')),
    ('construction', ('Construction')),
    ('consumerelectronics', ('Consumer Electronics')),
    ('consumergoods', ('Consumer Goods')),
    ('consumerservices', ('Consumer Services')),
    ('cosmetics', ('Cosmetics')),
    ('dairy', ('Dairy')),
    ('defense', ('Defense/Space')),
    ('design', ('Design')),
    ('e-learning', ('E-Learning')),
    ('educationmanagement', ('Education Management')),
    ('electrical', ('Electrical/Electronic Manufacturing')),
    ('energy', ('Energy')),
    ('entertainment', ('Entertainment/Movie Production')),
    ('environmentalservices', ('Environmental Services')),
    ('eventsservices', ('Events Services')),
    ('executiveoffice', ('Executive Office')),
    ('facilitiesservices', ('Facilities Services')),
    ('farming', ('Farming')),
    ('financialservices', ('Financial Services')),
    ('fineart', ('Fine Art')),
    ('fishery', ('Fishery')),
    ('foodproduction', ('Food Production')),
    ('food', ('Food/Beverages')),
    ('fundraising', ('Fundraising')),
    ('furniture', ('Furniture')),
    ('gambling', ('Gambling/Casinos')),
    ('glass', ('Glass/Ceramics/Concrete')),
    ('governmentadministration', ('Government Administration')),
    ('governmentrelations', ('Government Relations')),
    ('graphicdesign', ('Graphic Design/Web Design')),
    ('health', ('Health/Fitness')),
    ('highereducation', ('Higher Education/Acadamia')),
    ('hospital', ('Hospital/Health Care')),
    ('hospitality', ('Hospitality')),
    ('humanresources', ('Human Resources/HR')),
    ('import', ('Import/Export')),
    ('individual', ('Individual/Family Services')),
    ('industrialautomation', ('Industrial Automation')),
    ('informationservices', ('Information Services')),
    ('informationtechnology', ('Information Technology/IT')),
    ('insurance', ('Insurance')),
    ('internationalaffairs', ('International Affairs')),
    ('internationaltrade', ('International Trade/Development')),
    ('internet', ('Internet')),
    ('investmentbanking', ('Investment Banking/Venture')),
    ('investmentmanagement',
        ('Investment Management/Hedge Fund/Private Equity')),
    ('judiciary', ('Judiciary')),
    ('lawenforcement', ('Law Enforcement')),
    ('lawpractice', ('Law Practice/Law Firms')),
    ('legalservices', ('Legal Services')),
    ('legislativeoffice', ('Legislative Office')),
    ('leisure', ('Leisure/Travel')),
    ('library', ('Library')),
    ('logistics', ('Logistics/Procurement')),
    ('luxurygoods', ('Luxury Goods/Jewelry')),
    ('machinery', ('Machinery')),
    ('managementconsulting', ('Management Consulting')),
    ('maritime', ('Maritime')),
    ('marketresearch', ('Market Research')),
    ('marketing', ('Marketing/Advertising/Sales')),
    ('mechanicalindustrialengineering',
        ('Mechanical or Industrial Engineering')),
    ('mediaproduction', ('Media Production')),
    ('medicalequipment', ('Medical Equipment')),
    ('medicalpractice', ('Medical Practice')),
    ('mentalhealthcare', ('Mental Health Care')),
    ('militaryindustry', ('Military Industry')),
    ('mining', ('Mining/Metals')),
    ('motionpictures', ('Motion Pictures/Film')),
    ('museums', ('Museums/Institutions')),
    ('music', ('Music')),
    ('nanotechnology', ('Nanotechnology')),
    ('newspapers', ('Newspapers/Journalism')),
    ('non-profit', ('Non-Profit/Volunteering')),
    ('oil', ('Oil/Energy/Solar/Greentech')),
    ('onlinepublishing', ('Online Publishing')),
    ('otherindustry', ('Other Industry')),
    ('outsourcing', ('Outsourcing/Offshoring')),
    ('package', ('Package/Freight Delivery')),
    ('packaging', ('Packaging/Containers')),
    ('paper', ('Paper/Forest Products')),
    ('performingarts', ('Performing Arts')),
    ('pharmaceuticals', ('Pharmaceuticals')),
    ('philanthropy', ('Philanthropy')),
    ('photography', ('Photography')),
    ('plastics', ('Plastics')),
    ('politicalorganization', ('Political Organization')),
    ('primary', ('Primary/Secondary Education')),
    ('printing', ('Printing')),
    ('professionaltraining', ('Professional Training')),
    ('programdevelopment', ('Program Development')),
    ('publicrelations', ('Public Relations/PR')),
    ('publicsafety', ('Public Safety')),
    ('publishingindustry', ('Publishing Industry')),
    ('railroadmanufacture', ('Railroad Manufacture')),
    ('ranching', ('Ranching')),
    ('realestate', ('Real Estate/Mortgage')),
    ('recreationalfacilities', ('Recreational Facilities/Services')),
    ('religiousinstitutions', ('Religious Institutions')),
    ('renewables', ('Renewables/Environment')),
    ('researchindustry', ('Research Industry')),
    ('restaurants', ('Restaurants')),
    ('retailindustry', ('Retail Industry')),
     ('robotics', ('Robotics')),
    ('security', ('Security/Investigations')),
    ('semiconductors', ('Semiconductors')),
    ('shipbuilding', ('Shipbuilding')),
    ('software', ('Software / Web Applications')),
    ('sportinggoods', ('Sporting Goods')),
    ('sports', ('Sports')),
    ('staffing', ('Staffing/Recruiting')),
    ('supermarkets', ('Supermarkets')),
    ('telecommunications', ('Telecommunications')),
    ('textiles', ('Textiles')),
    ('thinktanks', ('Think Tanks')),
    ('tobacco', ('Tobacco')),
    ('translation', ('Translation/Localization')),
    ('transportation', ('Transportation')),
    ('utilities', ('Utilities')),
    ('venturecapital', ('Venture Capital/VC')),
    ('veterinary', ('Veterinary')),
    ('warehousing', ('Warehousing')),
    ('wholesale', ('Wholesale')),
    ('wine', ('Wine/Spirits')),
    ('wireless', ('Wireless')),
    ('writing', ('Writing/Editing')), 
)
class CreateOfferForm(forms.ModelForm):
    rfq = forms.ModelChoiceField(
        queryset = RFQ.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'RFQ No'}
        ),
    )
    part = forms.ModelChoiceField(
        queryset = Part.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Part No'}),
    )
    date = forms.DateField(
       required=True, 
       widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
    )
    status = forms.CharField(widget = forms.Select(
        choices=( ('gonderildi', 'Gönderildi'),
        ('inceleniyor', 'İnceleniyor')),
        attrs={'class': 'form-control'}))

    class Meta:
       
        model = Offer
        fields = '__all__'
        exclude = ['offer_no', 'created_date', 'related_person']


class CreateOfferRFQForm(forms.ModelForm):
    rfq = forms.ModelChoiceField(
        queryset = RFQ.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'RFQ No'}
        ),
    )
    part = forms.ModelChoiceField(
        queryset = Part.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Part No'}),
    )
    date = forms.DateField(
       required=True, 
       widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
    )
    status = forms.CharField(widget = forms.Select(
        choices=( ('gonderildi', 'Gönderildi'),
        ('inceleniyor', 'İnceleniyor')),
        attrs={'class': 'form-control'}))

    class Meta:
        model = Offer
        fields = '__all__'
        exclude =  ['offer_no', 'created_date', 'related_person']


class CreateRFQForm(forms.ModelForm):
    rfq_no = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Customer RFQ No'}),
        )
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=True, 
        widget = forms.Select(
            attrs={'class':'form-control', 'placeholder':'Customer'}
        )
    )
    request_date = forms.DateField(
       required=True, 
       widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
    )
    deadline = forms.DateField(
        required=False,
       widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
    )
    sent_date = forms.DateField(
         required=False,
       widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
    )
    part_quantity = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'placeholder':'Part Quantity'}
        )
    )
    status = forms.CharField(widget = forms.Select(
        choices=( ('sent', 'Sent'),
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('n/a', 'N/A')),
        attrs={'class': 'form-control'}))


    rfq_mail = forms.FileField(
         required=False,
        widget=forms.FileInput(
            attrs={'class':'form-control p-1 w-50'}
        )
    )


    class Meta:
        model = RFQ
        fields = '__all__'
        exclude = ['created_by', 'srv_rfq_no', 'created_date']

class CreateCustomerForm(forms.ModelForm):

    
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
        )
    
    country = CountryField().formfield(
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Address'}),
        )
    
    industry = forms.CharField(widget = forms.Select(
        choices=INDUSTRIES,
        attrs={'class': 'form-control'}))
    
    related_person_mail = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}),
        )
    
    status = forms.CharField(widget = forms.Select(
        choices=( 
        ('potansiyel', 'Potansiyel Müşteri'),
        ('mevcut', 'Mevcut Müşteri')
    ),
        attrs={'class': 'form-control'}))

    description = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Type some description'}),
        )

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['logo', 'created_date']


class CreatePartForm(forms.ModelForm):

    customer = forms.ModelChoiceField(
        queryset = Customer.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Customer'}
        ),
    ) 
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Part Name'}),
    )
    part_no = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Part No'}),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Something about the part'}),
    )
    unit_price = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'placeholder':'Unit Price'}
        )
    )
    mold_price = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(
            attrs={'class':'form-control', 'placeholder':'Mold Price'}
        )
    )


    class Meta:
        model = Part
        fields = '__all__'
        exclude = ['created_date']


class CreateOfferDetailForm(forms.ModelForm):
    class Meta:
        model = OfferDetail
        fields = '__all__'
        