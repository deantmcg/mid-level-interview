from datetime import datetime
from django.test import Client, TestCase

from .models import User, Server, Login

# Create your tests here.
class LoginsTestCase(TestCase):

    def setUp(self):

        # Create users
        u1 = User.objects.create(username="user1", full_name="User One")
        u2 = User.objects.create(username="user2", full_name="User Two")

        # Create servers
        s1 = Server.objects.create(name="server1", ip="228.230.136.212")
        s2 = Server.objects.create(name="server2", ip="203.253.113.187")

        # Create logins
        l1 = Login.objects.create(user=u1, server=s1, time=datetime.now())
        l2 = Login.objects.create(user=u2, server=s2, time=datetime(year=1900, month=1, day=1))

    def test_valid_login_date(self):
        l = Login.objects.get(user__username="user1")
        self.assertTrue(l.is_valid_login())

    def test_invalid_login_date(self):
        l = Login.objects.get(user__username="user2")
        self.assertFalse(l.is_valid_login())

    def test_server_logins_index(self):
        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["server_login_list"]), 2)
        self.assertEqual(len(response.context["server_login_list"][0]["logins"]), 1)
        self.assertEqual(len(response.context["server_login_list"][1]["logins"]), 1)