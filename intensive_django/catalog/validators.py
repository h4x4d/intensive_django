from functools import wraps

from django.forms import ValidationError


def validate_brilliant(value):
    need_words = {"превосходно", "роскошно"}
    check_value = value.lower()

    if not any([word in check_value for word in need_words]):
        raise ValidationError(
            f"Обязательно используйте слово {' или '.join(need_words)}")

    return value


def validate_must_be_param(*args):
    args = [i.lower() for i in args]

    @wraps(validate_must_be_param)
    def _inner(value):
        new_value = value.lower()

        if not any([word in new_value for word in args]):
            raise ValidationError(
                f"Обязательно используйте слово {' или '.join(args)}")

        return value

    return _inner
