from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    number = forms.CharField(
        max_length=11, 
        required=True, 
        help_text="شماره تلفن خود را وارد کنید (مثلا: 09123456789)",
        error_messages={
            'required': 'وارد کردن شماره تلفن الزامی است.',
            'max_length': 'شماره تلفن نمی‌تواند بیشتر از ۱۱ رقم باشد.'
        }
    )

    class Meta:
        model = User
        fields = ('username', 'number', 'password1', 'password2')
        error_messages = {
            'username': {
                'required': _('وارد کردن نام کاربری الزامی است.'),
                'unique': _('این نام کاربری قبلاً ثبت شده است.'),
            },
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        import re
        if not re.match(r'^09\d{9}$', number):
            raise forms.ValidationError('شماره تلفن باید با 09 شروع شود و 11 رقم باشد.')
        return number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # فارسی کردن پیام خطاهای پسورد
        self.fields['password1'].error_messages.update({
            'required': 'وارد کردن رمز عبور الزامی است.',
            'password_mismatch': 'رمز عبور با تکرار آن مطابقت ندارد.',
        })
        self.fields['password2'].error_messages.update({
            'required': 'تکرار رمز عبور الزامی است.'
        })



