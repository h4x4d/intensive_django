from django import forms
from feedback.models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('text', )

        labels = {
            'text': 'Текст обращения'
        }

        help_texts = {
            'text': 'Максимум: 1000 символов'
        }

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'То, что вы хотите'
                                                         ' нам сказать...'})
        }
