from django.db import models
class customManager(models.Manager):
    def get_queryset(self):          #======>all() => get_queryset()
        return super().get_queryset().order_by('eno')
    def get_emp_sal_range(self,esal1,esal2): #====> own method
        return super().get_queryset().filter(esal__range=(esal1,esal2))
        #views => employees.objects.get_emp_sal_range(10,200)
    def get_sort_by(self,parameter):
        return super().get_queryset().order_by(parameter)
         #views =>employees.objects.get_sort_by("ename")

class employees(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esalary=models.IntegerField()
    objects=customManager()