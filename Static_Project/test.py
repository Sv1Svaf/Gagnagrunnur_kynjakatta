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
