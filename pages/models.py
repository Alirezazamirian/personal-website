from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='Profile picture', blank=True, null=True, upload_to='personal_image/')
    long_description = models.TextField(max_length=300, verbose_name='About description', blank=True, null=True)
    short_description = models.TextField(max_length=20, verbose_name='Home description', blank=True, null=True)
    total_project = models.PositiveIntegerField(verbose_name='Total Project', blank=True, null=True)
    experience_year = models.PositiveIntegerField(verbose_name='Experience Year', blank=True, null=True)
    clients = models.PositiveIntegerField(verbose_name='Total clients', blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Education(models.Model):
    LEVEL_CHOICES = (
        ('bachelor', 'bachelor'),
        ('master', 'master'),
        ('PHD', 'PHD')
    )

    major = models.CharField(max_length=100, verbose_name='Major', blank=True, null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name='graduate level')
    university = models.CharField(max_length=100, verbose_name='university')
    start_year = models.PositiveIntegerField(verbose_name='start year')
    end_year = models.PositiveIntegerField(verbose_name='end year')
    about_education = models.TextField(max_length=300, verbose_name='about education')
    is_active = models.BooleanField(verbose_name='Is active', default=False)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return f'{self.level} of {self.major}'


class Experience(models.Model):
    company = models.CharField(max_length=100, verbose_name='Company name')
    position = models.CharField(max_length=100, verbose_name='Position')
    start_year = models.PositiveIntegerField(verbose_name='Start year')
    end_year = models.CharField(verbose_name='End year', max_length=100)
    about_experience = models.TextField(max_length=1000, verbose_name='About work experience')
    is_active = models.BooleanField(verbose_name='Is active', default=False)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def str_convertor(self):
        if self.end_year.lower() == 'now':
            now = date.today()
            return now.year
        else:
            return self.end_year

    def __str__(self):
        return f'{self.position} at {self.company} for {self.str_convertor() - self.start_year} years'


class Skills(models.Model):
    title = models.CharField(max_length=100, verbose_name='Skill title')
    percentage = models.PositiveIntegerField(verbose_name='Percentage')
    level = models.CharField(max_length=20, verbose_name='Level')
    is_active = models.BooleanField(verbose_name='Is active', default=False)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.title} is {self.level} with {self.percentage}% power'


class Awards(models.Model):
    title = models.CharField(max_length=100, verbose_name='Award')
    earn_year = models.DateField(verbose_name='Earned date')
    credit_link = models.URLField(verbose_name='Credit link')
    description = models.TextField(verbose_name='Description', max_length=200)
    is_active = models.BooleanField(verbose_name='Is active', default=False)

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    def __str__(self):
        return f'{self.title} in {self.earn_year}'


class MyOffer(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description', max_length=300)
    is_active = models.BooleanField(verbose_name='Is active', default=False)

    class Meta:
        verbose_name = 'My offer'
        verbose_name_plural = 'My offers'

    def __str__(self):
        return self.title


class MyBlog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(verbose_name='Image', upload_to='articles/')
    deployment_date = models.DateField(verbose_name='Deployment date', auto_now_add=True)
    description = models.TextField(verbose_name='Description', max_length=1000)
    is_active = models.BooleanField(verbose_name='Is active', default=False)
    comment = models.ForeignKey('CommentBlog', on_delete=models.CASCADE, verbose_name='Comment', blank=True, null=True,
                                related_name='comment')
    category = models.ForeignKey('CategoryBlog', on_delete=models.CASCADE, verbose_name='Category', blank=True,
                                 null=True, related_name='category')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    description = models.TextField(verbose_name='Description', max_length=100)
    comment_date = models.DateTimeField(verbose_name='Comment date', auto_now_add=True, editable=False)
    is_okay = models.BooleanField(verbose_name='Is okay', default=False)

    class Meta:
        verbose_name = 'Blog comment'
        verbose_name_plural = 'Blog comments'

    def __str__(self):
        return f'{self.name} with email : {self.email}'


class CategoryBlog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='URL Title')
    is_active = models.BooleanField(default=False, verbose_name='Is active')

    class Meta:
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    phone = models.CharField(max_length=100, verbose_name='Phone')
    email = models.CharField(max_length=100, verbose_name='Email')
    location = models.TextField(max_length=200, verbose_name='Location')
    site_logo = models.ImageField(verbose_name='Site image', upload_to='site_images/')
    footer_description = models.TextField(max_length=100, verbose_name='Footer description')
    instagram = models.URLField(verbose_name='Instagram', blank=True, null=True)
    telegram = models.URLField(verbose_name='Telegram', blank=True, null=True)
    linkedin = models.URLField(verbose_name='Linkedin', blank=True, null=True)
    github = models.URLField(verbose_name='Github', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='Is active')

    class Meta:
        verbose_name = 'Site setting'
        verbose_name_plural = 'Site settings'

    def __str__(self):
        return f'{self.phone} - {self.email}'


class Projects(models.Model):
    CHOICES = [
        ('Dynamic', 'Dynamic'),
        ('Static', 'Static')
    ]
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(verbose_name='Image', upload_to='projects/images/main')
    about_project = models.TextField(verbose_name='About project', max_length=200)
    deployment_year = models.DateField(verbose_name='Deployment year')
    client = models.CharField(verbose_name='Client', max_length=50)
    services = models.ForeignKey('Services', blank=True, null=True, verbose_name='Services', on_delete=models.CASCADE)
    project_type = models.CharField(verbose_name='Project type', max_length=100, choices=CHOICES)
    url = models.URLField(verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Services(models.Model):
    TYPES = [
        ('E-commerce website', 'E-commerce website'),
        ('Business website', 'Business website'),
        ('Media website', 'Media website'),
        ('Educational website', 'Educational website'),
        ('Membership website', 'Membership website'),
        ('Backend development', 'Backend development'),
        ('Architecture', 'Architecture'),
        ('Database design', 'Database design'),
        ('API development', 'API development'),
    ]

    title = models.CharField(max_length=100, verbose_name='Title', choices=TYPES)
    description = models.TextField(verbose_name='Description', max_length=100)
    is_main = models.BooleanField(default=False, verbose_name='Is main',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
