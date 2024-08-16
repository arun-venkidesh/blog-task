from django import forms
from blogtaskapp.models import poems

class PoemForm(forms.ModelForm):
    class Meta:
        model=poems
        fields = "__all__"