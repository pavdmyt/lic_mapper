from django import forms


class MapForm(forms.Form):
    ra_item = forms.CharField(max_length=20, label="RA item code")
