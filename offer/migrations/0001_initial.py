# Generated by Django 4.2.5 on 2023-09-25 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('industry', models.CharField(choices=[('accounting', 'Accounting'), ('airlines', 'Airlines/Aviation'), ('alternativemedicine', 'Alternative Medicine'), ('analyticsdata', 'Analytics / Data Science'), ('animation', 'Animation'), ('apparel', 'Apparel/Fashion'), ('architecture', 'Architecture/Planning'), ('arts', 'Arts/Crafts'), ('automotive', 'Automotive'), ('aviation', 'Aviation/Aerospace'), ('banking', 'Banking/Mortgage'), ('biotechnology', 'Biotechnology/Greentech'), ('broadcastmedia', 'Broadcast Media'), ('buildingmaterials', 'Building Materials'), ('businesssupplies', 'Business Supplies/Equipment'), ('capitalmarkets', 'Capital Markets/Hedge Fund/Private Equity'), ('chemicals', 'Chemicals'), ('civic', 'Civic/Social Organization'), ('civilengineering', 'Civil Engineering'), ('commercialrealestate', 'Commercial Real Estate'), ('computergames', 'Computer Games'), ('computerhardware', 'Computer Hardware'), ('computernetworking', 'Computer Networking'), ('computersoftware', 'Computer Software/Engineering'), ('computer', 'Computer/Network Security'), ('construction', 'Construction'), ('consumerelectronics', 'Consumer Electronics'), ('consumergoods', 'Consumer Goods'), ('consumerservices', 'Consumer Services'), ('cosmetics', 'Cosmetics'), ('dairy', 'Dairy'), ('defense', 'Defense/Space'), ('design', 'Design'), ('e-learning', 'E-Learning'), ('educationmanagement', 'Education Management'), ('electrical', 'Electrical/Electronic Manufacturing'), ('energy', 'Energy'), ('entertainment', 'Entertainment/Movie Production'), ('environmentalservices', 'Environmental Services'), ('eventsservices', 'Events Services'), ('executiveoffice', 'Executive Office'), ('facilitiesservices', 'Facilities Services'), ('farming', 'Farming'), ('financialservices', 'Financial Services'), ('fineart', 'Fine Art'), ('fishery', 'Fishery'), ('foodproduction', 'Food Production'), ('food', 'Food/Beverages'), ('fundraising', 'Fundraising'), ('furniture', 'Furniture'), ('gambling', 'Gambling/Casinos'), ('glass', 'Glass/Ceramics/Concrete'), ('governmentadministration', 'Government Administration'), ('governmentrelations', 'Government Relations'), ('graphicdesign', 'Graphic Design/Web Design'), ('health', 'Health/Fitness'), ('highereducation', 'Higher Education/Acadamia'), ('hospital', 'Hospital/Health Care'), ('hospitality', 'Hospitality'), ('humanresources', 'Human Resources/HR'), ('import', 'Import/Export'), ('individual', 'Individual/Family Services'), ('industrialautomation', 'Industrial Automation'), ('informationservices', 'Information Services'), ('informationtechnology', 'Information Technology/IT'), ('insurance', 'Insurance'), ('internationalaffairs', 'International Affairs'), ('internationaltrade', 'International Trade/Development'), ('internet', 'Internet'), ('investmentbanking', 'Investment Banking/Venture'), ('investmentmanagement', 'Investment Management/Hedge Fund/Private Equity'), ('judiciary', 'Judiciary'), ('lawenforcement', 'Law Enforcement'), ('lawpractice', 'Law Practice/Law Firms'), ('legalservices', 'Legal Services'), ('legislativeoffice', 'Legislative Office'), ('leisure', 'Leisure/Travel'), ('library', 'Library'), ('logistics', 'Logistics/Procurement'), ('luxurygoods', 'Luxury Goods/Jewelry'), ('machinery', 'Machinery'), ('managementconsulting', 'Management Consulting'), ('maritime', 'Maritime'), ('marketresearch', 'Market Research'), ('marketing', 'Marketing/Advertising/Sales'), ('mechanicalindustrialengineering', 'Mechanical or Industrial Engineering'), ('mediaproduction', 'Media Production'), ('medicalequipment', 'Medical Equipment'), ('medicalpractice', 'Medical Practice'), ('mentalhealthcare', 'Mental Health Care'), ('militaryindustry', 'Military Industry'), ('mining', 'Mining/Metals'), ('motionpictures', 'Motion Pictures/Film'), ('museums', 'Museums/Institutions'), ('music', 'Music'), ('nanotechnology', 'Nanotechnology'), ('newspapers', 'Newspapers/Journalism'), ('non-profit', 'Non-Profit/Volunteering'), ('oil', 'Oil/Energy/Solar/Greentech'), ('onlinepublishing', 'Online Publishing'), ('otherindustry', 'Other Industry'), ('outsourcing', 'Outsourcing/Offshoring'), ('package', 'Package/Freight Delivery'), ('packaging', 'Packaging/Containers'), ('paper', 'Paper/Forest Products'), ('performingarts', 'Performing Arts'), ('pharmaceuticals', 'Pharmaceuticals'), ('philanthropy', 'Philanthropy'), ('photography', 'Photography'), ('plastics', 'Plastics'), ('politicalorganization', 'Political Organization'), ('primary', 'Primary/Secondary Education'), ('printing', 'Printing'), ('professionaltraining', 'Professional Training'), ('programdevelopment', 'Program Development'), ('publicrelations', 'Public Relations/PR'), ('publicsafety', 'Public Safety'), ('publishingindustry', 'Publishing Industry'), ('railroadmanufacture', 'Railroad Manufacture'), ('ranching', 'Ranching'), ('realestate', 'Real Estate/Mortgage'), ('recreationalfacilities', 'Recreational Facilities/Services'), ('religiousinstitutions', 'Religious Institutions'), ('renewables', 'Renewables/Environment'), ('researchindustry', 'Research Industry'), ('restaurants', 'Restaurants'), ('retailindustry', 'Retail Industry'), ('security', 'Security/Investigations'), ('semiconductors', 'Semiconductors'), ('shipbuilding', 'Shipbuilding'), ('software', 'Software / Web Applications'), ('sportinggoods', 'Sporting Goods'), ('sports', 'Sports'), ('staffing', 'Staffing/Recruiting'), ('supermarkets', 'Supermarkets'), ('telecommunications', 'Telecommunications'), ('textiles', 'Textiles'), ('thinktanks', 'Think Tanks'), ('tobacco', 'Tobacco'), ('translation', 'Translation/Localization'), ('transportation', 'Transportation'), ('utilities', 'Utilities'), ('venturecapital', 'Venture Capital/VC'), ('veterinary', 'Veterinary'), ('warehousing', 'Warehousing'), ('wholesale', 'Wholesale'), ('wine', 'Wine/Spirits'), ('wireless', 'Wireless'), ('writing', 'Writing/Editing')], default='Automotive', max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('potansiyel', 'Potansiyel Müşteri'), ('mevcut', 'Mevcut Müşteri')], default='potansiyel', max_length=25)),
                ('related_person_mail', models.EmailField(max_length=254)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='RFQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfq_no', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('part_quantity', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('uygun', 'Uygun'), ('inceleniyor', 'İnceleniyor')], default='inceleniyor', max_length=25)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('part_no', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mold_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_no', models.CharField(max_length=25)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('gonderildi', 'Gönderildi'), ('inceleniyor', 'İnceleniyor')], default='inceleniyor', max_length=25)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.part')),
                ('related_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rfq_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.rfq')),
            ],
        ),
    ]
