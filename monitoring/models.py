from django.db import models

# USER MODEL
class User(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    full_name = models.CharField(max_length=80, null=False)
    phone_number = models.CharField(max_length=22)
    email = models.CharField(max_length=320)


# SERVER MODEL
class Server(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=15, unique=True, null=False)


# LOGIN MODEL
class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=False)
    time = models.DateTimeField(null=False)