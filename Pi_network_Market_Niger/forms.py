from django import forms

class searchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'size': '120'
                                    }
                                ))