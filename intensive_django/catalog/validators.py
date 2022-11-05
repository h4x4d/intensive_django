import re
from functools import wraps

from django.forms import ValidationError


def validate_brilliant(value):
    need_words = {"превосходно", "роскошно"}
    check_value = re.sub(r'[^\w\s]', ' ', value.lower())

    if len(need_words & set(check_value.split())) == 0:
        raise ValidationError(
            f"Обязательно используйте слово {' или '.join(need_words)}")

    return value


def validate_must_be_param(*args):
    args = {i.lower() for i in args}

    @wraps(validate_must_be_param)
    def _inner(value):
        check_value = re.sub(r'[^\w\s]', ' ', value.lower())

        if len(args & set(check_value.split())) == 0:
            raise ValidationError(
                f"Обязательно используйте слово {' или '.join(args)}")

        return value

    return _inner
