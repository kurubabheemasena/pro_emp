from django.db import models

# Create your models here.
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Employe(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(Department,on_delete=models.CASCADE)


    def __str__(self):
        return self.ename
