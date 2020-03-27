from django.core.management.base import BaseCommand, no_translations
from accounts.models import AccountRequests
from django.db.models import Count
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Notify sponsors of new account requests'

    def handle(self, *args, **options):
        pending_notifications = AccountRequests.objects.filter(sponsor_notified=False).values('sponsor__email').annotate(
            total=Count('sponsor__email'))

        for notification in pending_notifications:
            results = send_mail(
                'Pending GeoPlatform Account Requests',
                f'{notification["total"]} GeoPlatform Account Request(s) is pending your approval in the GeoPlatform Account Request Tool(request.ercloud.org).'
                f'Please log in to the <a href="https://request.ercloud.org/accounts/list">GeoPlatform Account Request Tool Approval List</a> to configure new GeoPlatform accounts and notify the users when configuration is complete.',
                'GIS_Team@epa.gov',
                [notification['sponsor__email']],
                fail_silently=False,
                html_message=f'{notification["total"]} GeoPlatform Account Request(s) is pending your approval in the GeoPlatform Account Request Tool(request.ercloud.org).'
                f'Please log in to the <a href="https://request.ercloud.org/accounts/list">GeoPlatform Account Request Tool Approval List</a> to configure new GeoPlatform accounts and notify the users when configuration is complete.',
            )
            if results == 1:
                AccountRequests.objects.filter(
                    sponsor_notified=False,
                    sponsor__email=notification['sponsor__email']
                ).update(sponsor_notified=True)
