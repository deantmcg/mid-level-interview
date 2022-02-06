from django.shortcuts import render
from .models import Login, Server

# Create your views here.
def logins(request):
    server_logins_list = []
    servers = Server.objects.all()

    for server in servers:
        login_list = Login.objects.filter(server__id=server.id).order_by('time')
        server_logins_list.append({'details': server, 'logins': login_list})

    return render(request, 'monitoring/logins.html', {'server_login_list': server_logins_list})