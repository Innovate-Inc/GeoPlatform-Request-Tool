# Generated by Django 2.2.24 on 2021-12-03 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_groupmembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='responseproject',
            name='default_reason',
            field=models.CharField(choices=[('Emergency Response', 'Emergency Response'), ('Other Federal Agency', 'Other Federal Agency'), ('State Agency', 'State Agency'), ('University', 'University'), ('Long Term GIS Support', 'Long Term GIS Support'), ('Non Government Organization', 'Non Government Organization'), ('Tribal Government', 'Tribal Government'), ('Citizen Advisor', 'Citizen Advisor'), ('Other', 'Other')], default='Emergency Response', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountrequests',
            name='reason',
            field=models.CharField(blank=True, choices=[('Emergency Response', 'Emergency Response'), ('Other Federal Agency', 'Other Federal Agency'), ('State Agency', 'State Agency'), ('University', 'University'), ('Long Term GIS Support', 'Long Term GIS Support'), ('Non Government Organization', 'Non Government Organization'), ('Tribal Government', 'Tribal Government'), ('Citizen Advisor', 'Citizen Advisor'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='accountrequests',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='requests', to='accounts.ResponseProject'),
        ),
        migrations.AlterField(
            model_name='responseproject',
            name='is_disabled',
            field=models.BooleanField(default=False, help_text='Setting this will send an email notification to assigned sponsors and their delegates.'),
        ),
    ]