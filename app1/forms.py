from django import forms

class CountryForm(forms.Form):
    name = forms.CharField(label='Country', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Country'}))