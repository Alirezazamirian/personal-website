# Generated by Django 5.0.4 on 2024-04-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_awards_options_alter_categoryblog_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('location', models.TextField(max_length=200, verbose_name='Location')),
                ('site_logo', models.ImageField(upload_to='site_images/', verbose_name='Site image')),
                ('footer_description', models.TextField(max_length=100, verbose_name='Footer description')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
                ('github', models.URLField(blank=True, null=True, verbose_name='Github')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Site setting',
                'verbose_name_plural': 'Site settings',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='github',
        ),
        migrations.RemoveField(
            model_name='user',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='user',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telegram',
        ),
    ]