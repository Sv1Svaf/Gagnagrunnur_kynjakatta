from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from catdb.models import *
from .forms import SearchCat
# Create your views here.

def index(request,self):
	template = loader.get_template('kkidb/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def search(request,isSafe = True):
	template = loader.get_template('kkidb/search.html')
	form = SearchCat()
	context = {
		'form': form,
		'isSafe':isSafe
		}
	return HttpResponse(template.render(context, request))

def findcat(request):
	c = cat.objects.all()
	req = request.GET
	valid = False
	#****************** Name **************
	if(req.get('name') != ''):
		valid = True
		c = c.filter(name__contains = req.get('name'))
	#****************** Registered number **************
	if(req.get('reg_nr') != ''):
		valid = True
		c = c.filter(reg_nr = req.get('reg_nr'))
	#****************** GENDER *********************
	if(req.get('gender') != None):
		valid = True
		c = c.filter(gender = eval(req.get('gender')))
	# ***************** Birth lookup *************
	if(req.get('birth_year') != '0'):
		valid = True
		c = c.filter(birth__year = req.get('birth_year'))
	if(req.get('birth_month') != '0'):
		valid = True
		c = c.filter(birth__month = req.get('birth_month'))
	if(req.get('birth_day') != '0'):
		valid = True
		c = c.filter(birth__day = req.get('birth_day'))
	# **************** Registered lookup *************
	if(req.get('registered_year') != '0'):
		valid = True
		c = c.filter(registered__year = req.get('registered_year'))
	if(req.get('registered_month') != '0'):
		valid = True
		c = c.filter(registered__month = req.get('registered_month'))
	if(req.get('registered_day') != '0'):
		valid = True
		c = c.filter(registered__day = req.get('registered_day'))	
	# *************** Dam and Sire ********************
	if(req.get('dam') != ''):
		valid = True
		for cats in c[:]:
			P = cats.dam
			if(P == None or P.cat == None or (not (req.get('dam') in P.cat.name))):
				c = c.exclude(name = cats.name)
	if(req.get('sire') != ''):
		valid = True
		for cats in c[:]:
			P = cats.sire
			if(P == None or P.cat == None or (not (req.get('sire') in P.cat.name))):
				c = c.exclude(name = cats.name)
	#**************** Roundup *****************
	if(len(c) > 0):
		template = loader.get_template('kkidb/results.html')
		context = {
			'cats': c,
		}
		return HttpResponse(template.render(context, request))
	else:
		return search(request,False)

def kitty(request):
    C = cat.objects.all()
    template = loader.get_template('kkidb/testpage.html')
    context = {
        'cats': C,
    }
    return HttpResponse(template.render(context, request))

def catview(request):
	template = loader.get_template('kkidb/ViewCat.html')
	view = request.GET.get('view')
	if(view != ''):
		c = cat.objects.all()
		c = c.filter(id = view)
	if(len(c) != 1):
		context = {}
	else:
		context ={
				'cat'  : c[0]
			}

	return HttpResponse(template.render(context, request))

def fourohfour(request):
	template = loader.get_template('kkidb/404.html')
	context = {}
	return HttpResponse(template.render(context, request))