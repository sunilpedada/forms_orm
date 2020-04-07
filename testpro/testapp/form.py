from django import forms
from testapp.models import players
class player_form(forms.ModelForm):
    class Meta:
        model=players
        fields="__all__"