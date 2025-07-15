from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    number = forms.CharField(
        max_length=11,
        required=True,
        help_text="مثلاً: 09123456789",
        label="شماره موبایل",
        error_messages={
            'required': 'وارد کردن شماره تلفن الزامی است.',
            'max_length': 'شماره تلفن نمی‌تواند بیشتر از ۱۱ رقم باشد.'
        }
    )

    class Meta:
        model = User
        fields = ('username', 'number', 'password1', 'password2')
        labels = {
            'username': 'نام کاربری',
            'password1': 'رمز عبور',
            'password2': 'تکرار رمز عبور',
        }
        error_messages = {
            'username': {
                'required': 'وارد کردن نام کاربری الزامی است.',
                'unique': 'این نام کاربری قبلاً ثبت شده است.',
            },
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        import re
        if not re.match(r'^09\d{9}$', number):
            raise forms.ValidationError('شماره تلفن باید با ۰۹ شروع شود و دقیقاً ۱۱ رقم باشد.')
        return number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تکرار رمز عبور'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = 'بین ۴ تا ۱۵ کاراکتر، فقط حروف و اعداد مجازند.'

        # فارسی‌سازی پیام‌های خطای رمز عبور
        self.fields['password1'].error_messages.update({
            'required': 'وارد کردن رمز عبور الزامی است.',
        })
        self.fields['password2'].error_messages.update({
            'required': 'تکرار رمز عبور الزامی است.',
        })
