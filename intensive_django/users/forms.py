from django import forms

from users.models import Account


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def save(self, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'birthday')

        widgets = {
            Account.birthday.field.name: forms.DateTimeInput(
                attrs={'type': 'date'}),
        }


