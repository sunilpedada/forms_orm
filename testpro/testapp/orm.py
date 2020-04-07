from testapp.models import players
# //////////////////////////////// ORM ////////////////////////////////////
queryset=players.objects.all() #======>all records type()=>queryset
employe=players.objects.get(id=10)  #=======>emplye object()
print(queryset)
print(str(queryset.query)) #=====> to know internal queryes
#--------------------------
#3) condition
players.objects.filter(esalary__gt=5000)#>5000

lookup_fields=[__gt,__gte,__lt,__lte]
#excat
players.objects.get(id__excat=12)
players.objects.get(ename__excat='dhoni')
players.objects.get(id__iexcat=12)# case in sensitive
players.objects.filter(ename__contains='dhoni')
players.objects.filter(ename__icontains="Dhoni")
players.objects.filter(id__in=[1,2,3,55])
players.objects.filter(ename__istartswith='s')
players.objects.filter(ename__iendswith='s')
players.objects.filter(esalary__range=(200,8000))
#/////// or condition /////
obj=players.objects.filter(ename__startswith='s')|players.objects.filter(esalary__gt=5000)
from django.db.models import Q
obj=players.objects.filter(Q(ename__startswith='s')|q(esalary__range=(50,500)))
#//// and condition ////
obj=players.objects.filter(ename__startswith='s',esalary__range=(50,500))
obj=players.objects.filter(Q(ename__startswith='s')&Q(esalary__range=(50,500)))
#//// not ///////
obj=players.objects.exclude(esalary__range=(50,500))
players.objects.filter(~Q(esalary__range=(50,500)))
#////////////// working with multipultabels ////////////
#/////////// union  /////////////////////////
a=players.objects.filter(ename__startswith='l')
b=matches.objects.filter(escore__gt=5000)       #=======>(both tebles should have same colums and names)    
c=a.union(b)      
players.objects.all().values_list("name","email")
#/////////// agrregate /////////
from django.db.models import Avg,Sum,Min,Max,Count
players.objects.all().aggegate(Avg('esalary'))  
players.objects.all().order_by("esalary")
players.objects.all().order_by("-esalary")[0]     
from django.db.models.functions import Lower
players.objects.all().order_by(Lower("ename"))         
#///////////// model inheritance //////////
# abstract base inheritance,multitable,multiple a,b,c(a,b),multi level                                                         