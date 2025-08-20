from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class TrainingRegistration(models.Model):
    child_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+79991234567'"
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="Номер телефона"
    )
    planned_date = models.DateTimeField(verbose_name="Планируемая дата")
    agreement = models.BooleanField(verbose_name="Согласие на обработку данных")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.child_name} - {self.phone_number}"