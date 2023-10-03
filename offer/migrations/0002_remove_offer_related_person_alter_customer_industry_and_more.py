# Generated by Django 4.2.5 on 2023-09-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='related_person',
        ),
        migrations.AlterField(
            model_name='customer',
            name='industry',
            field=models.CharField(choices=[('accounting', 'Accounting'), ('airlines', 'Airlines/Aviation'), ('alternativemedicine', 'Alternative Medicine'), ('analyticsdata', 'Analytics / Data Science'), ('animation', 'Animation'), ('apparel', 'Apparel/Fashion'), ('architecture', 'Architecture/Planning'), ('arts', 'Arts/Crafts'), ('automotive', 'Automotive'), ('aviation', 'Aviation/Aerospace'), ('banking', 'Banking/Mortgage'), ('biotechnology', 'Biotechnology/Greentech'), ('broadcastmedia', 'Broadcast Media'), ('buildingmaterials', 'Building Materials'), ('businesssupplies', 'Business Supplies/Equipment'), ('capitalmarkets', 'Capital Markets/Hedge Fund/Private Equity'), ('chemicals', 'Chemicals'), ('civic', 'Civic/Social Organization'), ('civilengineering', 'Civil Engineering'), ('commercialrealestate', 'Commercial Real Estate'), ('computergames', 'Computer Games'), ('computerhardware', 'Computer Hardware'), ('computernetworking', 'Computer Networking'), ('computersoftware', 'Computer Software/Engineering'), ('computer', 'Computer/Network Security'), ('construction', 'Construction'), ('consumerelectronics', 'Consumer Electronics'), ('consumergoods', 'Consumer Goods'), ('consumerservices', 'Consumer Services'), ('cosmetics', 'Cosmetics'), ('dairy', 'Dairy'), ('defense', 'Defense/Space'), ('design', 'Design'), ('e-learning', 'E-Learning'), ('educationmanagement', 'Education Management'), ('electrical', 'Electrical/Electronic Manufacturing'), ('energy', 'Energy'), ('entertainment', 'Entertainment/Movie Production'), ('environmentalservices', 'Environmental Services'), ('eventsservices', 'Events Services'), ('executiveoffice', 'Executive Office'), ('facilitiesservices', 'Facilities Services'), ('farming', 'Farming'), ('financialservices', 'Financial Services'), ('fineart', 'Fine Art'), ('fishery', 'Fishery'), ('foodproduction', 'Food Production'), ('food', 'Food/Beverages'), ('fundraising', 'Fundraising'), ('furniture', 'Furniture'), ('gambling', 'Gambling/Casinos'), ('glass', 'Glass/Ceramics/Concrete'), ('governmentadministration', 'Government Administration'), ('governmentrelations', 'Government Relations'), ('graphicdesign', 'Graphic Design/Web Design'), ('health', 'Health/Fitness'), ('highereducation', 'Higher Education/Acadamia'), ('hospital', 'Hospital/Health Care'), ('hospitality', 'Hospitality'), ('humanresources', 'Human Resources/HR'), ('import', 'Import/Export'), ('individual', 'Individual/Family Services'), ('industrialautomation', 'Industrial Automation'), ('informationservices', 'Information Services'), ('informationtechnology', 'Information Technology/IT'), ('insurance', 'Insurance'), ('internationalaffairs', 'International Affairs'), ('internationaltrade', 'International Trade/Development'), ('internet', 'Internet'), ('investmentbanking', 'Investment Banking/Venture'), ('investmentmanagement', 'Investment Management/Hedge Fund/Private Equity'), ('judiciary', 'Judiciary'), ('lawenforcement', 'Law Enforcement'), ('lawpractice', 'Law Practice/Law Firms'), ('legalservices', 'Legal Services'), ('legislativeoffice', 'Legislative Office'), ('leisure', 'Leisure/Travel'), ('library', 'Library'), ('logistics', 'Logistics/Procurement'), ('luxurygoods', 'Luxury Goods/Jewelry'), ('machinery', 'Machinery'), ('managementconsulting', 'Management Consulting'), ('maritime', 'Maritime'), ('marketresearch', 'Market Research'), ('marketing', 'Marketing/Advertising/Sales'), ('mechanicalindustrialengineering', 'Mechanical or Industrial Engineering'), ('mediaproduction', 'Media Production'), ('medicalequipment', 'Medical Equipment'), ('medicalpractice', 'Medical Practice'), ('mentalhealthcare', 'Mental Health Care'), ('militaryindustry', 'Military Industry'), ('mining', 'Mining/Metals'), ('motionpictures', 'Motion Pictures/Film'), ('museums', 'Museums/Institutions'), ('music', 'Music'), ('nanotechnology', 'Nanotechnology'), ('newspapers', 'Newspapers/Journalism'), ('non-profit', 'Non-Profit/Volunteering'), ('oil', 'Oil/Energy/Solar/Greentech'), ('onlinepublishing', 'Online Publishing'), ('otherindustry', 'Other Industry'), ('outsourcing', 'Outsourcing/Offshoring'), ('package', 'Package/Freight Delivery'), ('packaging', 'Packaging/Containers'), ('paper', 'Paper/Forest Products'), ('performingarts', 'Performing Arts'), ('pharmaceuticals', 'Pharmaceuticals'), ('philanthropy', 'Philanthropy'), ('photography', 'Photography'), ('plastics', 'Plastics'), ('politicalorganization', 'Political Organization'), ('primary', 'Primary/Secondary Education'), ('printing', 'Printing'), ('professionaltraining', 'Professional Training'), ('programdevelopment', 'Program Development'), ('publicrelations', 'Public Relations/PR'), ('publicsafety', 'Public Safety'), ('publishingindustry', 'Publishing Industry'), ('railroadmanufacture', 'Railroad Manufacture'), ('ranching', 'Ranching'), ('realestate', 'Real Estate/Mortgage'), ('recreationalfacilities', 'Recreational Facilities/Services'), ('religiousinstitutions', 'Religious Institutions'), ('renewables', 'Renewables/Environment'), ('researchindustry', 'Research Industry'), ('restaurants', 'Restaurants'), ('retailindustry', 'Retail Industry'), ('robotics', 'Robotics'), ('security', 'Security/Investigations'), ('semiconductors', 'Semiconductors'), ('shipbuilding', 'Shipbuilding'), ('software', 'Software / Web Applications'), ('sportinggoods', 'Sporting Goods'), ('sports', 'Sports'), ('staffing', 'Staffing/Recruiting'), ('supermarkets', 'Supermarkets'), ('telecommunications', 'Telecommunications'), ('textiles', 'Textiles'), ('thinktanks', 'Think Tanks'), ('tobacco', 'Tobacco'), ('translation', 'Translation/Localization'), ('transportation', 'Transportation'), ('utilities', 'Utilities'), ('venturecapital', 'Venture Capital/VC'), ('veterinary', 'Veterinary'), ('warehousing', 'Warehousing'), ('wholesale', 'Wholesale'), ('wine', 'Wine/Spirits'), ('wireless', 'Wireless'), ('writing', 'Writing/Editing')], default='Automotive', max_length=100),
        ),
        migrations.AlterField(
            model_name='rfq',
            name='rfq_no',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
