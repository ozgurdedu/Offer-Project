from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.contrib.auth.models import User


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
class Customer(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    industry = models.CharField(choices=INDUSTRIES, max_length=100, default="Automotive")
    address = models.CharField(max_length =255)
    related_person_mail = models.EmailField()
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=25, choices=(
            ('potansiyel', 'Potansiyel Müşteri'),
            ('mevcut', 'Mevcut Müşteri')
        ), default="potansiyel"
    )
    logo = models.ImageField(upload_to="static/img", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class Part(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    part_no = models.CharField(max_length=50, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    mold_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.part_no


class RFQ(models.Model):
    
    rfq_no = models.CharField(max_length=50, null=True, blank=True)
    srv_rfq_no = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_date = models.DateField(default=timezone.now)
    deadline = models.DateField(blank=True, null=True)
    sent_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    part_quantity = models.PositiveIntegerField(default=0)
    rfq_mail = models.FileField(upload_to ='uploads/% Y/% m/% d/', blank=True, null=True)
    status = models.CharField(max_length=25, choices=(
        ('sent', 'Sent'),
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('n/a', 'N/A')
    ), default="in progress"
    )

    def __str__(self):
        return self.srv_rfq_no


    def save(self,*args, **kwargs):
        
        #SRFQ{year}-0{0-id}
        count = RFQ.objects.filter(request_date__year = self.request_date.year).count() + 1
        lastId = "0"+str(count) if count < 10 else count
        year = self.request_date.year % 100

        lastRFQ = None
        try: 
            lastRFQ = RFQ.objects.order_by('-id')[0].srv_rfq_no
        except IndexError:
            pass
    
        srv_rfq_no = f'SRFQ{year}-0{lastId}'
        
        if lastRFQ is not None:
            if lastRFQ == srv_rfq_no:
                count += 1
                lastId = "0"+str(count) if count < 10 else count
                srv_rfq_no = f'SRFQ{year}-0{lastId}'
            
        self.srv_rfq_no = srv_rfq_no
        return super(RFQ, self).save(*args, **kwargs)




class Offer(models.Model):
    offer_no = models.CharField(max_length=25)
    rfq = models.ForeignKey(RFQ, on_delete=models.CASCADE, blank=True, null=True)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    related_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=25, choices=(
        ('gonderildi', 'Gönderildi'),
        ('inceleniyor', 'İnceleniyor')
    ), default='inceleniyor')


    def save(self, *args, **kwargs):
        if not self.offer_no:
            #offer_no yoksa yeni bir kayıt oluşturuyoruz
            count = Offer.objects.filter(
            date__year = self.date.year, 
            related_person__id = self.related_person.id).count() + 1
            
            lastId = "0"+str(count) if count < 10 else count
        
            first_letter = self.related_person.first_name[0]
            second_letter = self.related_person.last_name[0]
            year = self.date.year % 100
          
            last_offer = None
            
            try:
                last_offer = Offer.objects.order_by('-id')[0]   
            except IndexError:
                pass
          
            offer_no = f'{first_letter}{second_letter}{year}-{lastId}'
            if last_offer is not None:
                if offer_no == str(last_offer):
                    
                    count += 1
                    lastId = "0"+str(count) if count < 10 else count
                    offer_no = f'{first_letter}{second_letter} - {year}{lastId}'

            self.offer_no = offer_no
        super(Offer, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.offer_no
    