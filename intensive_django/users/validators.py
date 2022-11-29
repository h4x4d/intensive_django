from django.core.exceptions import ValidationError
from django.db.models.functions import datetime


def validate_birthday(date):
    if date > datetime.datetime.today().date():
        raise ValidationError('День рождения должен быть в прошлом!')
    elif datetime.datetime(year=1900, day=1, month=1).date() > date:
        raise ValidationError('Дата рождения должна быть позже 1900 года!')

    return date
