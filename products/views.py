from django.shortcuts import render
from .models import ServerPackage

def package_list(request):
    packages = ServerPackage.objects.all()
    return render(request, 'products/package_list.html', {'packages': packages})