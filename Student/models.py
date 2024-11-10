from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField('部门', max_length=20, default='', primary_key=True, unique=True)
    building = models.CharField('楼栋', max_length=15, default='')
    budget = models.DecimalField('预算', max_digits=12, decimal_places=2, default=0.0)
    cachet = models.CharField('公章', max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '学院部门'
        verbose_name_plural = '学院/部门'

    def __str__(self):
        return self.dept_name