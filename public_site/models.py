from django.db import models
from django.utils import timezone

class Directory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    blurb = models.TextField(blank=True)
    keywords = models.CharField(max_length=200, blank=True)
    x_marketing = models.TextField(blank=True)
    editor = models.CharField(max_length=200, default='Stuart McL')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subdirectories')
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bookscot_site_directory'  # for databases like PostgreSQL
            
class Article(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, default='Article')
    section = models.CharField(max_length=200, default='Main')
    content = models.TextField()
    keywords = models.CharField(max_length=200, blank=True)
    x_marketing = models.TextField(blank=True)
    author = models.CharField(max_length=200, default='Sue B')
    summary = models.TextField(blank=True)
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='articles')  
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Role(models.Model):
    role = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)

    SENIORITY_CHOICES = [
        ('Board', 'Board'),
        ('Executive', 'Executive'),
        ('Manager', 'Manager'), 
        ('Senior', 'Senior'),
        ('Junior', 'Junior'),
        ('Intern', 'Intern'),
        ('Staff', 'Staff'),
        ('Volunteer', 'Volunteer'),
        ('Public', 'Public'),
        ('Anonymous', 'Anonymous'),
    ]
    seniority = models.CharField(max_length=200, choices=SENIORITY_CHOICES, default='Anonymous')

    AUTHORISATION_CHOICES = [
        ('Full', 'Full'),
        ('Limited', 'Limited'),
        ('None', 'None'),
    ]
    authorisation = models.CharField(max_length=200, choices=AUTHORISATION_CHOICES, null=True)

    INFLUENCE_CHOICES = [
        ('Total', 'Total'),
        ('Max', 'Max'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Min', 'Min'),
        ('None', 'None'),
    ]
    influence = models.CharField(max_length=200, choices=INFLUENCE_CHOICES, null=True)

    def __str__(self):
        return self.role

class Personnel(models.Model):
    forename = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='personnel', null=True)
    biography = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    interests = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.forename} {self.surname}"

class ContactEntry(models.Model):
    forename = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

class ContactSubmission(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    url = models.URLField(blank=True)
    type_of_contact = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    page_id = models.CharField(max_length=100, blank=True)
    filepath = models.CharField(max_length=200, blank=True)
    datetime = models.DateTimeField()
    ip_address = models.GenericIPAddressField()
    browser_specs = models.TextField()

    def __str__(self):
        return f"{self.forename} {self.surname} - {self.type_of_contact}"
