from django import forms
from .models import Participants

class PostForm(forms.ModelForm):

    class Meta:
        model = Participants
        fields = '__all__'
        labels = {
            'name':'Name:',
            'surname':'Surname:',
            'company':'Company:',
            'title':'Title:',
            'country':'Country:',
            'tel':'Tel.:',
            'address':'Email:'
        }