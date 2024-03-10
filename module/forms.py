from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea)

from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=15)
    weight = forms.DecimalField(max_digits=5, decimal_places=2)
    height = forms.DecimalField(max_digits=5, decimal_places=2)
    gender = forms.CharField(max_length=1)

class FeedbackFormFunction(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=20)
    comments = forms.CharField(widget=forms.Textarea)