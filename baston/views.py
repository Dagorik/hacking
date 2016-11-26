from django.shortcuts import render, redirect
#from django.contrib.gis.geos import GEOSGeometry
from django.views.generic import View
from .models import Baston
from .forms import bastonForm
# Create your views here.

class BastonView(View):
  form = bastonForm()
  template = "baston.html"

  def get(self, request, *args, **kargs):
    return render(request, self.template,{"form":self.form})

  def post(self, request, *args, **kargs):
    self.form = batonForm(request.POST)

    if self.form.is_valid():
      baston = Baston() 
      baston.comentario = self.form.cleaned_data["comentario"]
      baston.save()
      return redirect("baston-list")
    
    return redirect("baston-post")
