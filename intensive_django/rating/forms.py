from django import forms
from rating.models import Rating


class SetRatingForm(forms.Form):
    options = ((0, 'Нет оценки'),
               (1, 'Ненавижу'),
               (2, 'Не нравится'),
               (3, 'Нормально'),
               (4, 'Нравится'),
               (5, 'Люблю'))

    rating = forms.ChoiceField(choices=options,
                               label='Ваша оценка:',
                               required=False,
                               )

    def save(self, user, item):
        cleaned_rating = self.cleaned_data['rating']
        if Rating.objects.filter(account_id=user.id,
                                 item_id=item.id).count() > 0:
            if self.cleaned_data['rating'] == '0':
                Rating.objects.filter(account_id=user.id,
                                      item_id=item.id).delete()
                return

            (Rating.objects.filter(account_id=user.id, item_id=item.id).
             update(rating=cleaned_rating))
            return

        Rating.objects.create(
            account_id=user.id, item_id=item.id,
            rating=cleaned_rating)
