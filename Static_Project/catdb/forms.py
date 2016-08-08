from django import forms 
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import extras

genderChoices = ((True,'Male'),(False,'Female'))
ImportedChoices = (('Imported','Imported'),)

class SearchCat(forms.Form):
	name = forms.CharField(
		required = False,max_length = 30
		)
	reg_nr = forms.CharField(
		required = False,
		label = "Reg_Nr",
		max_length = 50
		)
	gender = forms.ChoiceField(
		label = "gender",
		required = False, 
		widget = forms.RadioSelect,
		choices = genderChoices
		)
	birth = forms.DateField(widget=extras.SelectDateWidget(),required = False)
	registered = forms.DateField(widget=extras.SelectDateWidget(),required = False)
	sire = forms.CharField(
		label = "sire",
		max_length = 30,
		required = False
		)
	dam = forms.CharField(
		label = "dam", 
		max_length = 30, 
		required = False
		)
	microchip = forms.CharField(
		label = "chip",
		required = False,
		max_length = 30
		)
#	imp = forms.BooleanField(
#		label = "imported",
#		required = False
#		)
#	neut = forms.BooleanField(
#		label = "neutered",
#		required = False
#		)