from __future__ import unicode_literals

from django.db import models

# Create your models here.

class cat(models.Model):
	id = models.AutoField(primary_key = True)
	reg_nr = models.CharField(max_length = 5)
	name = models.CharField(max_length = 35)
	gender = models.BooleanField()
	birth = models.DateField()
	registered = models.DateField()
	dam = models.ForeignKey('parents',on_delete=models.CASCADE, related_name = 'dam',null=True,blank = True)
	sire = models.ForeignKey('parents',on_delete=models.CASCADE, related_name = 'sire',null = True,blank = True)
	comments = models.CharField(max_length = 144)
	type = models.CharField(max_length = 3)

class parents(models.Model):
	id = models.AutoField(primary_key = True)
	is_ghost = models.BooleanField()
	cat = models.ForeignKey('cat',on_delete = models.CASCADE,related_name = 'cat_id',null = True,blank = True)
	ghost = models.ForeignKey('ghost_cat',on_delete = models.CASCADE,related_name = 'ghost_id',null=True,blank = True)
	
class ghost_cat(models.Model):
	id = models.AutoField(primary_key = True)
	reg_nr = models.CharField(max_length = 30)
	name = models.CharField(max_length = 50)
	birth = models.DateField()
	microchip = models.CharField(max_length = 30)
	dam = models.ForeignKey('parents',on_delete = models.CASCADE,related_name='ghost_dam')
	sire = models.ForeignKey('parents',on_delete = models.CASCADE,related_name = 'ghost_sire')
	
class imp_cat(models.Model):
    id = models.AutoField(primary_key = True)
    cat = models.ForeignKey('cat',on_delete = models.CASCADE)
    org_country = models.CharField(max_length = 3,null = True)
    org_organization = models.CharField(max_length = 10,null = True)
    org_reg_nr = models.CharField(max_length = 20,null = True)

class EMS(models.Model):
	id = models.AutoField(primary_key = True)
	breed = models.CharField(max_length = 3)
	ems = models.CharField(max_length = 15)
	
class ghost_EMS(models.Model):
	id = models.AutoField(primary_key = True)
	ghost_cat = models.ForeignKey('ghost_cat',on_delete = models.CASCADE)
	ems = models.ForeignKey('EMS',on_delete = models.CASCADE)

class cat_EMS(models.Model):
	id = models.AutoField(primary_key = True)
	cat = models.ForeignKey('cat',on_delete = models.CASCADE)
	ems = models.ForeignKey('EMS',on_delete = models.CASCADE)
	reg_date = models.DateField(null = False)
	
class neutered(models.Model):
	id = models.AutoField(primary_key = True)
	cat = models.ForeignKey('cat',on_delete = models.CASCADE,null = False)
	date = models.DateField()
	
class microchip(models.Model):
	id = models.AutoField(primary_key = True)
	cat = models.ForeignKey('cat',on_delete = models.CASCADE)
	microchip_nr = models.CharField(max_length = 30)
	
