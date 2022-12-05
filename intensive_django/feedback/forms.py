from django import forms
from feedback.models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('text',)

        labels = {
            FeedBack.text.field.name: 'Текст обращения'
        }

        help_texts = {
            FeedBack.text.field.name: 'Максимум: 1000 символов'
        }

        widgets = {
            FeedBack.text.field.name: forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'То, что вы хотите'
                                      ' нам сказать...'})
        }
