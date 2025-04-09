from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
COUNTRIES = [
    ("AF", "Afghanistan"),
    ("AL", "Albania"),
    ("DZ", "Algeria"),
    ("AR", "Argentina"),
    ("AM", "Armenia"),
    ("AU", "Australia"),
    ("AT", "Austria"),
    ("AZ", "Azerbaijan"),
    ("BH", "Bahrain"),
    ("BD", "Bangladesh"),
    ("BY", "Belarus"),
    ("BE", "Belgium"),
    ("BZ", "Belize"),
    ("BJ", "Benin"),
    ("BT", "Bhutan"),
    ("BO", "Bolivia"),
    ("BA", "Bosnia and Herzegovina"),
    ("BW", "Botswana"),
    ("BR", "Brazil"),
    ("BN", "Brunei"),
    ("BG", "Bulgaria"),
    ("BF", "Burkina Faso"),
    ("BI", "Burundi"),
    ("KH", "Cambodia"),
    ("CM", "Cameroon"),
    ("CA", "Canada"),
    ("CV", "Cape Verde"),
    ("CF", "Central African Republic"),
    ("TD", "Chad"),
    ("CL", "Chile"),
    ("CN", "China"),
    ("CO", "Colombia"),
    ("KM", "Comoros"),
    ("CD", "Congo (Kinshasa)"),
    ("CG", "Congo (Brazzaville)"),
    ("CR", "Costa Rica"),
    ("CI", "Côte d'Ivoire"),
    ("HR", "Croatia"),
    ("CU", "Cuba"),
    ("CY", "Cyprus"),
    ("CZ", "Czech Republic"),
    ("DK", "Denmark"),
    ("DJ", "Djibouti"),
    ("DM", "Dominica"),
    ("DO", "Dominican Republic"),
    ("EC", "Ecuador"),
    ("EG", "Egypt"),
    ("SV", "El Salvador"),
    ("GQ", "Equatorial Guinea"),
    ("ER", "Eritrea"),
    ("EE", "Estonia"),
    ("SZ", "Eswatini"),
    ("ET", "Ethiopia"),
    ("FJ", "Fiji"),
    ("FI", "Finland"),
    ("FR", "France"),
    ("GA", "Gabon"),
    ("GM", "Gambia"),
    ("GE", "Georgia"),
    ("DE", "Germany"),
    ("GH", "Ghana"),
    ("GR", "Greece"),
    ("GD", "Grenada"),
    ("GT", "Guatemala"),
    ("GN", "Guinea"),
    ("GW", "Guinea-Bissau"),
    ("GY", "Guyana"),
    ("HT", "Haiti"),
    ("HN", "Honduras"),
    ("HU", "Hungary"),
    ("IS", "Iceland"),
    ("IN", "India"),
    ("ID", "Indonesia"),
    ("IR", "Iran"),
    ("IQ", "Iraq"),
    ("IE", "Ireland"),
    ("IL", "Israel"),
    ("IT", "Italy"),
    ("JM", "Jamaica"),
    ("JP", "Japan"),
    ("JO", "Jordan"),
    ("KZ", "Kazakhstan"),
    ("KE", "Kenya"),
    ("KI", "Kiribati"),
    ("KP", "Korea, North"),
    ("KR", "Korea, South"),
    ("KW", "Kuwait"),
    ("KG", "Kyrgyzstan"),
    ("LA", "Laos"),
    ("LV", "Latvia"),
    ("LB", "Lebanon"),
    ("LS", "Lesotho"),
    ("LR", "Liberia"),
    ("LY", "Libya"),
    ("LI", "Liechtenstein"),
    ("LT", "Lithuania"),
    ("LU", "Luxembourg"),
    ("MG", "Madagascar"),
    ("MW", "Malawi"),
    ("MY", "Malaysia"),
    ("MV", "Maldives"),
    ("ML", "Mali"),
    ("MT", "Malta"),
    ("MH", "Marshall Islands"),
    ("MR", "Mauritania"),
    ("MU", "Mauritius"),
    ("MX", "Mexico"),
    ("FM", "Micronesia"),
    ("MD", "Moldova"),
    ("MC", "Monaco"),
    ("MN", "Mongolia"),
    ("ME", "Montenegro"),
    ("MA", "Morocco"),
    ("MZ", "Mozambique"),
    ("MM", "Myanmar"),
    ("NA", "Namibia"),
    ("NR", "Nauru"),
    ("NP", "Nepal"),
    ("NL", "Netherlands"),
    ("NZ", "New Zealand"),
    ("NI", "Nicaragua"),
    ("NE", "Niger"),
    ("NG", "Nigeria"),
    ("NO", "Norway"),
    ("OM", "Oman"),
    ("PK", "Pakistan"),
    ("PW", "Palau"),
    ("PA", "Panama"),
    ("PG", "Papua New Guinea"),
    ("PY", "Paraguay"),
    ("PE", "Peru"),
    ("PH", "Philippines"),
    ("PL", "Poland"),
    ("PT", "Portugal"),
    ("QA", "Qatar"),
    ("RO", "Romania"),
    ("RU", "Russia"),
    ("RW", "Rwanda"),
    ("KN", "Saint Kitts and Nevis"),
    ("LC", "Saint Lucia"),
    ("VC", "Saint Vincent and the Grenadines"),
    ("WS", "Samoa"),
    ("SM", "San Marino"),
    ("ST", "Sao Tome and Principe"),
    ("SA", "Saudi Arabia"),
    ("SN", "Senegal"),
    ("RS", "Serbia"),
    ("SC", "Seychelles"),
    ("SL", "Sierra Leone"),
    ("SG", "Singapore"),
    ("SK", "Slovakia"),
    ("SI", "Slovenia"),
    ("SB", "Solomon Islands"),
    ("SO", "Somalia"),
    ("ZA", "South Africa"),
    ("SS", "South Sudan"),
    ("ES", "Spain"),
    ("LK", "Sri Lanka"),
    ("SD", "Sudan"),
    ("SR", "Suriname"),
    ("SE", "Sweden"),
    ("CH", "Switzerland"),
    ("SY", "Syria"),
    ("TW", "Taiwan"),
    ("TJ", "Tajikistan"),
    ("TZ", "Tanzania"),
    ("TH", "Thailand"),
    ("TL", "Timor-Leste"),
    ("TG", "Togo"),
    ("TO", "Tonga"),
    ("TT", "Trinidad and Tobago"),
    ("TN", "Tunisia"),
    ("TR", "Turkey"),
    ("TM", "Turkmenistan"),
    ("TV", "Tuvalu"),
    ("UG", "Uganda"),
    ("UA", "Ukraine"),
    ("AE", "United Arab Emirates"),
    ("GB", "United Kingdom"),
    ("US", "United States"),
    ("UY", "Uruguay"),
    ("UZ", "Uzbekistan"),
    ("VU", "Vanuatu"),
    ("VA", "Vatican City"),
    ("VE", "Venezuela"),
    ("VN", "Vietnam"),
    ("YE", "Yemen"),
    ("ZM", "Zambia"),
    ("ZW", "Zimbabwe"),
]

class Users(AbstractUser):
    username = models.CharField(max_length=20, unique=True, null=False, blank=False, validators=[], verbose_name="Username") 
    country = models.CharField(max_length=50, choices=COUNTRIES, null=False, blank=False, verbose_name="Country")
    profession = models.CharField(max_length=50, null=False, blank=False, default="Unemployed", verbose_name="Profession") #validator
    avatar = models.ImageField(verbose_name="Profile picture", default="default_profile.png", upload_to="users_profile_pictures/")
    #works
    phone = models.IntegerField(blank=False, null=True, verbose_name="Phone number")
    #links
    banned = models.BooleanField(default=False, verbose_name="Banned")
    #messages model for user
    info = models.TextField(null=True, blank=True, verbose_name="Additional info")
    moder = models.BooleanField(default=False, verbose_name='Moderator')
    twostepauth = models.BooleanField(default=False, verbose_name='2 step authentication')

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

        indexes = [
            models.Index(fields=['username', 'moder', 'profession'])
        ]

class Works(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='works')
    name = models.CharField(max_length=30, null=True, blank=False, verbose_name="Portfolio name")
    speciality = models.CharField(max_length=50, null=True, blank=False, verbose_name="Speciality")
    screenshots = models.ImageField(validators=[], verbose_name="Images")
    files = models.FileField(validators=[], verbose_name="Files")
    description = models.TextField(max_length=2000, null=True, blank=False, verbose_name="Description")
    comments = models.CharField(max_length=200) #comments model for comments 

    def __str__(self):
        return f"{self.user} {self.name}"
    
    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

        indexes = [ 
            models.Index(fields=['user', 'speciality', 'name']) 
        ]

class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Recipient", related_name="received_messages")
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Time')
    topic = models.CharField(max_length=30, null=True, blank=False, verbose_name='Message topic')
    message_text = models.CharField(max_length=255, null=True, blank=False, verbose_name='Message text')

    def __str__(self):
        return f"From {self.sender} to {self.user} at {self.date}."
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
