from django.db.models import Model
from django.shortcuts import render
from .models import Place, team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj2})





