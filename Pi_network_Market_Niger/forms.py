from django import forms

class searchForm(forms.Form):
    search = forms.CharField(label='search', max_length=100)