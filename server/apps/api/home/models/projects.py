from django.db import models
from django.contrib.auth import get_user_model
from ...employee_info.models.employee import Employee

class Project(models.Model):

    class Status(models.TextChoices):
        ANALYTIC = 'AL', 'Аналитика'
        DEVELOPMENT = 'DP', 'Разработка'
        TESTING = 'TT', 'Тестирование'
        COMPLETED = 'CL', 'Завершен'

    name = models.CharField(max_length=250,
                            verbose_name='Название проекта')
    
    slug = models.SlugField(unique=True,
                            verbose_name='Слаг')
    
    ###########################################
    #               Add employees             #
    ###########################################

    last_modify_user = models.ForeignKey(Employee,
                                         related_name='project',
                                         on_delete=models.SET_NULL,
                                         verbose_name='Последние изменения от',
                                         null = True)
    
    start_date = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата начала')
    
    last_modify_date = models.DateTimeField(auto_now=True,
                                            verbose_name='Дата последнего изменения')
    
    progress = models.DecimalField(default=0,
                                   max_digits=4,
                                   decimal_places=2,
                                   verbose_name='прогресс')
    
    deadline = models.DateField(verbose_name='Дедлайн')

    status = models.CharField(max_length=4,
                              choices=Status.choices,
                              default=Status.ANALYTIC,
                              verbose_name='Статус')
    
    class Meta():
        ordering = ["-id"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def str(self) -> str:
        return self.name