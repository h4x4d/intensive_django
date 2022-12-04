from catalog.models import Item
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import Account


class Rating(models.Model):
    item = models.ForeignKey(Item, verbose_name='товар',
                             on_delete=models.CASCADE)
    account = models.ForeignKey(Account, verbose_name='аккаунт',
                                on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='оценка',
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])

    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'
