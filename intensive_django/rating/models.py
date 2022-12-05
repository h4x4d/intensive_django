from catalog.models import Item
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import Account


class RatingModelManager(models.Manager):
    def filter_by_item(self, item_id):
        return self.get_queryset().filter(item_id=item_id)

    def get_rating_from_user(self, item_id, account_id):
        return self.get_queryset().get(item_id=item_id, account_id=account_id)


class Rating(models.Model):
    item = models.ForeignKey(Item, verbose_name='товар',
                             on_delete=models.CASCADE)
    account = models.ForeignKey(Account, verbose_name='аккаунт',
                                on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='оценка',
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])

    objects = RatingModelManager()

    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'
        constraints = [
            models.UniqueConstraint(
                fields=['item', 'account'], name='unique rating'),
        ]
