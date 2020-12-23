# Generated by Django 3.1.3 on 2020-12-10 21:37

from django.db import migrations


class Migration(migrations.Migration):

    def create_default_account_creation(apps, schema_editor):
        AccountCreation = apps.get_model('sequences', 'AccountCreation')

        AccountCreation.objects.create(integration_type='google')
        AccountCreation.objects.create(integration_type='slack')
        AccountCreation.objects.create(integration_type='asana')

    dependencies = [
        ('sequences', '0009_auto_20201210_1559'),
    ]

    operations = [
        migrations.RunPython(create_default_account_creation),
    ]