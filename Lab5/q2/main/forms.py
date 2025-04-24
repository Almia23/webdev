from django import forms

EMP_IDS = [('E101', 'E101'), ('E102', 'E102'), ('E103', 'E103')]

class PromoForm(forms.Form):
    emp_id = forms.ChoiceField(choices=EMP_IDS)
    doj = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))