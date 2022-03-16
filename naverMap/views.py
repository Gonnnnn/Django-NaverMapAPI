from django.shortcuts import render

from naverMap.models import CigCollector

# Create your views here.
def showMap(request):
    collectors = CigCollector.objects.all()
    return render(request, 'naverMap/naverMap.html', context={'collectors': collectors})