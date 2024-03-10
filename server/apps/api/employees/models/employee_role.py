from django.db import models

class Role(models.TextChoices):
    DEVELOPER = "DL", "Разработчик"
    ANALYST = "AL", "Аналитик"
    TESTER = "TT", "Тестировщик"

    



