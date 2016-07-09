from polls.models import Test
print('mesad')
entry_list = list(Test.objects.all())
print('memoresad')
for i in xrange(len(entry_list)):
    print(i)
    print(entry_list[i].Name)

print('ENDLINE')


