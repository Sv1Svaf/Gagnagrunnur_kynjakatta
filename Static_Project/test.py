from catdb.models import *
from django.utils import timezone
print("Test 1, works")

cc = cat()
cc.reg_nr = '123456789'
cc.name = 'Mjása'
cc.gender = True
cc.birth = timezone.now()
cc.registered = timezone.now()
cc.dam = None
cc.sire = None
cc.comments = None
cc.type = 'hsc'
cc.save()

c2 = cat()
c2.reg_nr = '2006952919'
c2.name = 'Eldrikarl'
c2.gender = False
c2.birth = timezone.now()
c2.registered = timezone.now()
c2.dam = None
c2.sire = None
c2.comments = 'A parent cat'
c2.type = 'hsc'
c2.save()

connection = parents()
connection.is_ghost = False
connection.cat = c2
connection.ghost = None

connection.save()
cc.sire = connection
cc.save()
