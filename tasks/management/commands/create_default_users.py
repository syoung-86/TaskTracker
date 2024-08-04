from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@test.com', 'plain-password')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser "admin"'))

        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user('testuser', 'test@test.com', 'plain-password')
            self.stdout.write(self.style.SUCCESS('Successfully created user "other_user"'))
