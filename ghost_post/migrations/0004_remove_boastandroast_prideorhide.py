# Generated by Django 2.2.7 on 2019-12-18 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghost_post', '0003_boastandroast_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastandroast',
            name='prideorhide',
        ),
    ]