from django.db import models

class Schedule(models.Model):
    class id(models.TextChoices):
        BEFORE_LUNCH = "BL", "До обеда"
        LUNCH = "LC", "Перерыв"
        AFTER_LUNCH = "AL", "После обеда"
        AFTER_WORK = "AW", "После работы"

    timeline_id = models.CharField(
        max_length=3,
        choices=id.choices,
        verbose_name="Временной интервал",
    )

    name = models.CharField(
        max_length=128,
        verbose_name="Описание"
    )

    hours = models.PositiveIntegerField(
        verbose_name="Кол-во часов"
    )
    
    class Meta():
        verbose_name = "График"
        verbose_name_plural = "Графики"
