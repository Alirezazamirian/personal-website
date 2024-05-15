# Generated by Django 5.0.4 on 2024-04-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_myblog_deployment_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awards',
            options={'verbose_name': 'Award', 'verbose_name_plural': 'Awards'},
        ),
        migrations.AlterModelOptions(
            name='categoryblog',
            options={'verbose_name': 'Blog category', 'verbose_name_plural': 'Blog categories'},
        ),
        migrations.AlterModelOptions(
            name='commentblog',
            options={'verbose_name': 'Blog comment', 'verbose_name_plural': 'Blog comments'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
        migrations.AlterModelOptions(
            name='myblog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='myoffer',
            options={'verbose_name': 'My offer', 'verbose_name_plural': 'My offers'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Major'),
        ),
    ]