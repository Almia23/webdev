from django import forms

class CaptchaForm(forms.Form):
    input_text = forms.CharField(label="Enter Captcha")