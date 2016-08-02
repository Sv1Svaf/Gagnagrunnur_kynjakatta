from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from catdb.models import *
# Create your views here.

def index(request,self):
	template = loader.get_template('kkidb/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
def cats(request):
    C = cat.objects.all()
    template = loader.get_template('kkidb/testpage.html')
    context = {
        'cats': C,
    }
    return HttpResponse(template.render(context, request))