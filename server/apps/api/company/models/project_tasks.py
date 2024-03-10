from django.db import models
from models.project import Project

class Task(models.Model):

    class StatusTask(models.TextChoices):
        TODO = "TD", "Надо сделать"
        IN_PROGRESS = "IP", "В работе"
        DONE = "DN", "Выполнен"

    title = models.CharField(max_length=250, verbose_name = 'Название')

    descripion = models.TextField(verbose_name = 'Описание')

    # type_task = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Тип задачи")

    task_start = models.DateField(auto_now_add=True, verbose_name = 'Начало задачи')

    task_end = models.DateField(verbose_name = 'Конец задачи')

    status = models.CharField(max_length = 4, choices = StatusTask.choices, default = StatusTask.TODO)

    project = models.ForeignKey(Project, related_name="task", on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self) -> str:
        return self.title
