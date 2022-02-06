from monitoring.models import User, Server, Login
from django.core.management import BaseCommand
import csv
from dateutil import parser


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data/logins.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None) # skip headers
            
            for line in csv_reader:
                existing = self.get_existing_login(line)

                if existing is None:
                    s = self.get_server(line[0], line[1])
                    u = self.get_user(line[2], line[3], line[4])
                    l = Login(
                        user = u,
                        server = s,
                        time = self.convert_date(line[5])
                    )

                    s.save()
                    u.save()
                    l.save()
                else:
                    self.set_user_contact(existing.user, line[5])
                    existing.user.save()

    def get_existing_login(self, csv_line):
        try:
            s = Server.objects.get(ip = csv_line[1])
            u = User.objects.get(username = csv_line[2])
            login = Login.objects.get(
                        server = s,
                        user = u,
                        time = self.convert_date(csv_line[5])
                    )
            return login
        except (Server.DoesNotExist, User.DoesNotExist, Login.DoesNotExist):
            return None

    def get_server(self, name, ip):
        try:
            s = Server.objects.get(ip = ip)
            return s
        except Server.DoesNotExist:
            return Server(
                        name = name,
                        ip = ip
                    )

    def get_user(self, username, full_name, contact_details):
        try:
            u = User.objects.get(username = username)
            return u
        except User.DoesNotExist:
            u = User(
                        username = username,
                        full_name = full_name
                    )
            self.set_user_contact(u, contact_details)
            return u

    def set_user_contact(self, user, contact_details):
        if '@' in contact_details:
            user.email = contact_details
        elif contact_details != '':
            user.phone_number = contact_details

    def convert_date(self, date_str):
        date_str = date_str.replace("\\", "/").replace("|", "/")
        try:
            return parser.parse(date_str)
        except:
            # dd/YY/MM > dd/MM/YY
            new_date = date_str.split('/')
            new_date = new_date[0] + new_date[2] + new_date[1]
            return parser.parse(new_date)
