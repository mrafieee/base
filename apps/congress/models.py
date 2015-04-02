from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import date
import os
from isecho.settings import LANGUAGES

COUNTRY_CHOICES = (('Afghanistan', _('Afghanistan')), ('Albania', _('Albania')), ('Algeria', _('Algeria')), ('Andorra', _('Andorra')), ('Angola', _('Angola')), ('Antigua and Barbuda', _('Antigua and Barbuda')), ('Argentina', _('Argentina')), ('Armenia', _('Armenia')), ('Australia', _('Australia')), ('Austria', _('Austria')), ('Azerbaijan', _('Azerbaijan')), ('Bahamas, The', _('Bahamas, The')), ('Bahrain', _('Bahrain')), ('Bangladesh', _('Bangladesh')), ('Barbados', _('Barbados')), ('Belarus', _('Belarus')), ('Belgium', _('Belgium')), ('Belize', _('Belize')), ('Benin', _('Benin')), ('Bhutan', _('Bhutan')), ('Bolivia', _('Bolivia')), ('Bosnia and Herzegovina', _('Bosnia and Herzegovina')), ('Botswana', _('Botswana')), ('Brazil', _('Brazil')), ('Brunei', _('Brunei')), ('Bulgaria', _('Bulgaria')), ('Burkina Faso', _('Burkina Faso')), ('Burma', _('Burma')), ('Burundi', _('Burundi')), ('Cambodia', _('Cambodia')), ('Cameroon', _('Cameroon')), ('Canada', _('Canada')), ('Cape Verde', _('Cape Verde')), ('Central African Republic', _('Central African Republic')), ('Chad', _('Chad')), ('Chile', _('Chile')), ('China', _('China')), ('Colombia', _('Colombia')), ('Comoros', _('Comoros')), ('Congo (Brazzaville)', _('Congo (Brazzaville)')), ('Congo (Kinshasa)', _('Congo (Kinshasa)')), ('Costa Rica', _('Costa Rica')), ('Cote d\'Ivoire', _('Cote d\'Ivoire')), ('Croatia', _('Croatia')), ('Cuba', _('Cuba')), ('Cyprus', _('Cyprus')), ('Czech Republic', _('Czech Republic')), ('Denmark', _('Denmark')), ('Djibouti', _('Djibouti')), ('Dominica', _('Dominica')), ('Dominican Republic', _('Dominican Republic')), ('East Timor (see Timor-Leste)', _('East Timor (see Timor-Leste)')), ('Ecuador', _('Ecuador')), ('Egypt', _('Egypt')), ('El Salvador', _('El Salvador')), ('Equatorial Guinea', _('Equatorial Guinea')), ('Eritrea', _('Eritrea')), ('Estonia', _('Estonia')), ('Ethiopia', _('Ethiopia')), ('Fiji', _('Fiji')), ('Finland', _('Finland')), ('France', _('France')), ('Gabon', _('Gabon')), ('Gambia, The', _('Gambia, The')), ('Georgia', _('Georgia')), ('Germany', _('Germany')), ('Ghana', _('Ghana')), ('Greece', _('Greece')), ('Grenada', _('Grenada')), ('Guatemala', _('Guatemala')), ('Guinea', _('Guinea')), ('Guinea-Bissau', _('Guinea-Bissau')), ('Guyana', _('Guyana')), ('Haiti', _('Haiti')), ('Holy See', _('Holy See')), ('Honduras', _('Honduras')), ('Hong Kong', _('Hong Kong')), ('Hungary', _('Hungary')), ('Iceland', _('Iceland')), ('India', _('India')), ('Indonesia', _('Indonesia')), ('Iran', _('Iran')), ('Iraq', _('Iraq')), ('Ireland', _('Ireland')), ('Israel', _('Israel')), ('Italy', _('Italy')), ('Jamaica', _('Jamaica')), ('Japan', _('Japan')), ('Jordan', _('Jordan')), ('Kazakhstan', _('Kazakhstan')), ('Kenya', _('Kenya')), ('Kiribati', _('Kiribati')), ('Korea, North', _('Korea, North')), ('Korea, South', _('Korea, South')), ('Kosovo', _('Kosovo')), ('Kuwait', _('Kuwait')), ('Kyrgyzstan', _('Kyrgyzstan')), ('Laos', _('Laos')), ('Latvia', _('Latvia')), ('Lebanon', _('Lebanon')), ('Lesotho', _('Lesotho')), ('Liberia', _('Liberia')), ('Libya', _('Libya')), ('Liechtenstein', _('Liechtenstein')), ('Lithuania', _('Lithuania')), ('Luxembourg', _('Luxembourg')), ('Macau', _('Macau')), ('Macedonia', _('Macedonia')), ('Madagascar', _('Madagascar')), ('Malawi', _('Malawi')), ('Malaysia', _('Malaysia')), ('Maldives', _('Maldives')), ('Mali', _('Mali')), ('Malta', _('Malta')), ('Marshall Islands', _('Marshall Islands')), ('Mauritania', _('Mauritania')), ('Mauritius', _('Mauritius')), ('Mexico', _('Mexico')), ('Micronesia', _('Micronesia')), ('Moldova', _('Moldova')), ('Monaco', _('Monaco')), ('Mongolia', _('Mongolia')), ('Montenegro', _('Montenegro')), ('Morocco', _('Morocco')), ('Mozambique', _('Mozambique')), ('Namibia', _('Namibia')), ('Nauru', _('Nauru')), ('Nepal', _('Nepal')), ('Netherlands', _('Netherlands')), ('Netherlands Antilles', _('Netherlands Antilles')), ('New Zealand', _('New Zealand')), ('Nicaragua', _('Nicaragua')), ('Niger', _('Niger')), ('Nigeria', _('Nigeria')), ('North Korea', _('North Korea')), ('Norway', _('Norway')), ('Oman', _('Oman')), ('Pakistan', _('Pakistan')), ('Palau', _('Palau')), ('Palestinian Territories', _('Palestinian Territories')), ('Panama', _('Panama')), ('Papua New Guinea', _('Papua New Guinea')), ('Paraguay', _('Paraguay')), ('Peru', _('Peru')), ('Philippines', _('Philippines')), ('Poland', _('Poland')), ('Portugal', _('Portugal')), ('Qatar', _('Qatar')), ('Romania', _('Romania')), ('Russia', _('Russia')), ('Rwanda', _('Rwanda')), ('Saint Kitts and Nevis', _('Saint Kitts and Nevis')), ('Saint Lucia', _('Saint Lucia')), ('Saint Vincent and the Grenadines', _('Saint Vincent and the Grenadines')), ('Samoa', _('Samoa')), ('San Marino', _('San Marino')), ('Sao Tome and Principe', _('Sao Tome and Principe')), ('Saudi Arabia', _('Saudi Arabia')), ('Senegal', _('Senegal')), ('Serbia', _('Serbia')), ('Seychelles', _('Seychelles')), ('Sierra Leone', _('Sierra Leone')), ('Singapore', _('Singapore')), ('Slovakia', _('Slovakia')), ('Slovenia', _('Slovenia')), ('Solomon Islands', _('Solomon Islands')), ('Somalia', _('Somalia')), ('South Africa', _('South Africa')), ('South Korea', _('South Korea')), ('Spain', _('Spain')), ('Sri Lanka', _('Sri Lanka')), ('Sudan', _('Sudan')), ('Suriname', _('Suriname')), ('Swaziland', _('Swaziland')), ('Sweden', _('Sweden')), ('Switzerland', _('Switzerland')), ('Syria', _('Syria')), ('Taiwan', _('Taiwan')), ('Tajikistan', _('Tajikistan')), ('Tanzania', _('Tanzania')), ('Thailand', _('Thailand')), ('Timor-Leste', _('Timor-Leste')), ('Togo', _('Togo')), ('Tonga', _('Tonga')), ('Trinidad and Tobago', _('Trinidad and Tobago')), ('Tunisia', _('Tunisia')), ('Turkey', _('Turkey')), ('Turkmenistan', _('Turkmenistan')), ('Tuvalu', _('Tuvalu')), ('Uganda', _('Uganda')), ('Ukraine', _('Ukraine')), ('United Arab Emirates', _('United Arab Emirates')), ('United Kingdom', _('United Kingdom')), ('Uruguay', _('Uruguay')), ('Uzbekistan', _('Uzbekistan')), ('Vanuatu', _('Vanuatu')), ('Venezuela', _('Venezuela')), ('Vietnam', _('Vietnam')), ('Yemen', _('Yemen')), ('Zambia', _('Zambia')), ('Zimbabwe', _('Zimbabwe')))	
STATUS_CHOICES = ((0, _('Pending')), (1,_('Rejected')), (2,_('Accepted')))
TITLE_CHOICES = (
	('', _('Select title')),
	('Cardiac Surgeon', _('Cardiac Surgeon')),
	('Cardiologist, Sub Special', _('Cardiologist, Sub Special')),
	('Cardiac Anesthesiologisd', _('Cardiac Anesthesiologisd')), 
	('Thoracic Surgeon', _('Thoracic Surgeon')),
	('Other Sub Special', _('Other Sub Special')),
	('Cardiologist', _('Cardiologist')), 
	('Anesthesiologist', _('Anesthesiologist')), 
	('General Surgeon', _('General Surgeon')), 
	('Residency and Felowship', _('Residency and Felowship')), 
	('Other Special', _('Other Special')), 
	('GP', _('GP')), 
	('Perfusionist', _('Perfusionist')), 
	('Rehabilitation', _('Rehabilitation')), 
	('Nurse', _('Nurse')), 
	('Technician', _('Technician')), 
	('Others', _('Others')), 
	)
		
class Congress(models.Model):
    PRIORITY_CHOICES = ((1,'1 (highest priority)'),(2,2),(3,3),(4,4),(5,'5 (lowest priority)'),)
    def get_image_path(instance, filename):
        return 'uploads/congress/%s/%s' % (instance.slug, filename)
    class Meta:
        verbose_name = _('Congress')
        verbose_name_plural = _('Congresses')
        db_table = 'congress'

    language = models.CharField(max_length=6, blank=False, choices=LANGUAGES, default="en")
    name = models.CharField(_('name'), max_length=250)
    slug = models.SlugField(_('Slug'))
    is_open = models.BooleanField(_('Open'),default=0, help_text=_('Check if Members can register on this congress'))
    opening_date = models.DateField(_('Opening Date'), default=date.today())
    closing_date = models.DateField(_('Closing Date'), default=date.today())
    registration_phone = models.CharField(_('Registration Phone'), max_length=100, blank=True, null=True)
    registration_fax = models.CharField(_('Registration Fax'), max_length=100, blank=True, null=True)
    early_registration = models.DateField(_('Early Registration'),  blank=True, null=True)
    late_registration = models.DateField(_('Late Registration'),  blank=True, null=True)
    online_registration = models.DateField(_('Online Registration'),  blank=True, null=True)
    address = models.CharField(_('Address'), max_length=200, blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    fee = models.TextField(_('Fee'), blank=True, null=True)
    poster = models.ImageField(_('Poster'), upload_to=get_image_path, blank=True, null=True)
    venue = models.ImageField(_('venue'), upload_to=get_image_path, help_text=_('Image - krooki'), blank=True, null=True)
    physician_articles_abstract = models.FileField(_('Physician Articles Abstract'), upload_to=get_image_path, help_text=_('PDF - pezeshki'), blank=True, null=True)
    paramedics_articles_abstract = models.FileField(_('Paramedics Articles Abstract'), upload_to=get_image_path, help_text=_('PDF - pira-pezeshki'), blank=True, null=True)
    sessions_program = models.FileField(_('Sessions Program'), upload_to=get_image_path, help_text=_('PDF - barname jalasat'), blank=True, null=True)
    priority = models.IntegerField(_('Priority'), default=1,choices=PRIORITY_CHOICES)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return '/congress/%s'%self.slug

class BoardDirectory(models.Model):
	def get_image_path(instance, filename):
		return 'uploads/congress/%s/board/%s' % (instance.congress.slug, filename)
	class Meta:
		verbose_name = _('Board Directory')
		verbose_name_plural = _('Board Directories')
	BOARD_TITLE_CHOICES = (
		('', _('None')),
		('Chairman of the Congress', _('Chairman of the Congress')),
		('Vice Chairman of the Congress', _('Vice Chairman of the Congress')),
		('Scientific Secretary', _('Scientific Secretary')),
		('Scientific Secretary of Cardiac Surgery', _('Scientific Secretary of Cardiac Surgery')), 
		('Scientific Secretary of Cardiology', _('Scientific Secretary of Cardiology')),
		('Executive Secretary', _('Executive Secretary')),)
	congress = models.ForeignKey(Congress)
	name = models.CharField(_('Board full name'), max_length=100)
	title = models.CharField(_('Title'), max_length=100, choices=BOARD_TITLE_CHOICES, blank=True, null=True)	
	photo = models.ImageField(_('Photo'), upload_to=get_image_path, blank=True, null=True)
	def __unicode__(self):
		return self.name

class Article(models.Model):
	class Meta:
		verbose_name = _('Submited Article')
		verbose_name_plural = _('Submited Articles')
		
	def get_image_path(instance, filename):
		return 'uploads/congress/%s/members/%s' % (instance.congress.slug, filename)
	TOPIC_CHOICES = (
		('', _('Select title')),
		('Adult and Pediatric Perfusion', _('Adult and Pediatric Perfusion')),
		('Adult Cardiology', _('Adult Cardiology')),
		('Adult Cardiovascular Surgery', _('Adult Cardiovascular Surgery')),
		('Cardiac Imaging', _('Cardiac Imaging')),
		('Cardiac Nursing', _('Cardiac Nursing')),
		('Cardiac physiotherapy and Rehabilitation', _('Cardiac physiotherapy and Rehabilitation')),
		('Electrophysiology', _('Electrophysiology')),
		('Endo vascular therapeutics', _('Endo vascular therapeutics')),
		('Heart Transplant', _('Heart Transplant')),
		('Hybrid Operation', _('Hybrid Operation')),
		('Interventional Cardiology', _('Interventional Cardiology')),
		('Minimally invasive cardiac surgery', _('Minimally invasive cardiac surgery')),
		('Pediatric Cardiology', _('Pediatric Cardiology')),
		('Pediatric Cardiovascular Surgery', _('Pediatric Cardiovascular Surgery')),
		('Preventive Cardiology', _('Preventive Cardiology')),
		('Stem Cell', _('Stem Cell')),
		('Other', _('Other')),)
	
	congress = models.ForeignKey(Congress)
	first_name = models.CharField(_('First Name'), max_length=100)
	last_name = models.CharField(_('Last Name'), max_length=100)
	email = models.CharField(_('e-mail'), max_length=100)
	phone = models.CharField(_('Phone'), max_length=100)
	postal_address = models.CharField(_('Postal Address'), max_length=100)
	affiliation = models.CharField(_('Affiliation'), max_length=100, blank=True, null=True)
	main_topic = models.CharField(_('Main Topic'), max_length=100, choices=TOPIC_CHOICES)
	abstract_title = models.CharField(_('Abstract Title'), max_length=100)
	authors = models.CharField(_('Authors'), max_length=100)
	abstract = models.TextField(_('Abstract'))
	code = models.CharField(_('Code'), unique=True, max_length=100)
	status = models.IntegerField(_('Status'), choices=STATUS_CHOICES,default=0)	
	attachment = models.FileField(_('Attachment'), upload_to=get_image_path, help_text=_('PDF - DOC'), blank=True, null=True)


	def __unicode__(self):
		return self.abstract_title

class Media(models.Model):
    def save(self, *args, **kwargs):
        self.type = self.get_type(self.file)
        # from middleware import threadlocals0
        # if threadlocals.get_current_user().is_authenticated():
        # self.user = threadlocals.get_current_user()
        super(Media, self).save(*args, **kwargs)

    def get_type(self, file):
        type = 'unknown'
        (dir, file) = os.path.split(str(file))

        (file_name, extension) = os.path.splitext(file)
        extension = extension.lower()
        for type in self.EXTENSIONS:
            if extension in type[1]:
                type = type[0]
                break
        return type

    def get_path(instance, filename):
        filename = "uploads/congress/"+ instance.congress.slug + "/" + filename
        return filename

    EXTENSIONS = (
        ('image', ('.jpg', '.gif', '.png', '.bmp', '.jpeg')),
        ('video', ('.flv', '.wmv')),  # Done
        ('flash', ('.swf',)),  # Done
        ('sound', ('.mp3', '.wma')),  # Done
        ('doc', ('.doc', '.docx',)),  # Done
        ('powerpoint', ('.ppt', '.pptx', '.pps')),  # Done
        ('excel', ('.xls', '.xlsx')),  # Done
        ('text', ('.txt',)),  # Done
        ('pdf', ('.pdf',)),  # Done
        ('archive', ('.zip', '.rar', '.7z', '.gz', '.bz2')),  # Done
        'unknown'  # Done
    )
    file = models.FileField(_('File'), upload_to=get_path)
    thumb = models.FileField(_('File Thumbnail'), upload_to=get_path, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(_('Description'), max_length=256, blank=True, null=True)
    congress = models.ForeignKey(Congress, blank=True, null=True)

    class Meta:
        ordering = ('file',)

    def __unicode__(self):
        return str(self.file)