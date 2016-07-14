from __future__ import unicode_literals

from django.db import models

# Create your models here.

class cat(models.Model):
	id = models.AutoField(primary_key = True)
	reg_nr = models.CharField(max_length = 30)
	name = models.CharField(max_length = 50)
	gender = models.BooleanField()
	birth = models.DateField()
	registered = models.DateField()
	dam = models.ForeignKey('parents',on_delete=models.CASCADE, related_name = 'dam',null=True,blank = True)
	sire = models.ForeignKey('parents',on_delete=models.CASCADE, related_name = 'sire',null = True,blank = True)
	comments = models.CharField(max_length = 50)
	type = models.CharField(max_length = 3)

class parents(models.Model):
	id = models.AutoField(primary_key = True)
	is_gost = models.BooleanField()
	_Cat = models.ForeignKey('cat',on_delete = models.CASCADE)
	_Ghost = models.ForeignKey('ghost_cat',on_delete = models.CASCADE)
	
class ghost_cat(models.Model):
	id = models.AutoField(primary_key = True)
	reg_nr = models.CharField(max_length = 30)
	name = models.CharField(max_length = 50)
	birth = models.DateField()
	ems = models.CharField(max_length = 20)
	microchip = models.CharField(max_length = 30)
	dam = models.ForeignKey('parents',on_delete = models.CASCADE,related_name='ghost_dam')
	sire = models.ForeignKey('parents',on_delete = models.CASCADE,related_name = 'ghost_sire')
	

