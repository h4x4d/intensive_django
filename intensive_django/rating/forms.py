from django import forms
from rating.models import Rating


class SetRatingForm(forms.Form):
    widget = forms.Select(attrs={'class': 'dropdown'})

    rating = forms.ChoiceField(choices=((0, 'Нет оценки'),
                                        (1, 'Ненавижу'),
                                        (2, 'Не нравится'),
                                        (3, 'Нормально'),
                                        (4, 'Нравится'),
                                        (5, 'Люблю')
                                        ),
                               label='Ваша оценка:',
                               required=False,
                               )

    def save(self, user, item):
        print(self.cleaned_data['rating'])
        if Rating.objects.filter(account_id=user.id,
                                 item_id=item.id).count() > 0:
            if self.cleaned_data['rating'] == '0':
                print('delete')
                Rating.objects.filter(account_id=user.id,
                                      item_id=item.id).delete()
            else:
                print('update')
                (Rating.objects.filter(account_id=user.id, item_id=item.id).
                 update(
                    rating=self.cleaned_data['rating']))
        else:
            Rating.objects.create(
                account_id=user.id, item_id=item.id,
                rating=self.cleaned_data['rating'])
