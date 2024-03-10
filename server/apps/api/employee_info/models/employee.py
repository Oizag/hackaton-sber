from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Employee(models.Model):

    class Status(models.TextChoices):
        CONFIRMED = "CF", 'Принят'
        UNCONFIRMED = "UCF", "Не принят"
    

    class Role(models.TextChoices):
        DEVELOPER = "DL", "Разработчик"
        ANALYST = "AL", "Аналитик"
        TESTER = "TT", "Тестировщик"


    name = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name="Работник")
    

    slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг')
    
    email = models.EmailField(max_length=250,
                              verbose_name="Почта")
    
    project_role = models.CharField(max_length=3,
                                    choices=Role.choices,
                                    verbose_name="Должноть")
    
    reservation_percent = models.DecimalField(max_digits=4,
                                              decimal_places=2,
                                              default=0,
                                              verbose_name="Загруженность работника")
    
    reservation_status = models.CharField(max_length=3,
                                          choices=Status.choices,
                                          default=Status.UNCONFIRMED,
                                          verbose_name="Статус")

    class Meta():
        verbose_name= "Работника"
        verbose_name_plural = "Работники"

    def __str__(self):
        return str(self.name)
    # def str(self) -> str:
    #     return f"{self.email}"