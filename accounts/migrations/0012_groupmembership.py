# Generated by Django 2.2.12 on 2021-02-19 21:39

from django.db import migrations, models
import django.db.models.deletion

def transfer_relationship_records(apps, schema_editor):
    AccountRequests = apps.get_model('accounts', 'AccountRequests')
    GroupMembership = apps.get_model('accounts', 'GroupMembership')
    for ar in AccountRequests.objects.all():
        for rel in AccountRequests.groups.through.objects.filter(accountrequests=ar):
            GroupMembership.objects.update_or_create(group=rel.agolgroup, request=rel.accountrequests, is_member=True)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210217_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_member', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AGOLGroup')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AccountRequests')),
            ],
        ),
        migrations.AddField(
            model_name='accountrequests',
            name='temp_groups',
            field=models.ManyToManyField(blank=True, related_name='account_requests',
                                         through='accounts.GroupMembership', to='accounts.AGOLGroup'),
        ),
        migrations.AddField(
            model_name='agolgroup',
            name='temp_requests',
            field=models.ManyToManyField(through='accounts.GroupMembership', to='accounts.AccountRequests'),
        ),
        migrations.RunPython(transfer_relationship_records, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='accountrequests',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='agolgroup',
            name='requests',
        ),
        migrations.RenameField(
            model_name='accountrequests',
            old_name='temp_groups',
            new_name='groups',
        ),
        migrations.RenameField(
            model_name='agolgroup',
            old_name='temp_requests',
            new_name='requests',
        ),
    ]