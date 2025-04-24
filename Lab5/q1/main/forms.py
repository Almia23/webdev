from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea)
    contact = forms.CharField()
    email = forms.EmailField()
    english = forms.IntegerField()
    physics = forms.IntegerField()
    chemistry = forms.IntegerField()