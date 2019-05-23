from django import forms
from .models import Reserve

class ReserveForm(forms.ModelForm):
    name  = forms.CharField(widget=forms.TextInput(
        attrs={
            'maxlength':'50',
            'type':'text',
            'class':'form-control',
            'id':'inputName',
            'placeholder':'Name'

        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
           'maxlength':'60',
           'type':'email',
            'class':'form-control',
            'id':'inputEmail',
            'placeholder':'Email'
        })
    )
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'maxlength':'20',
            'type':'tel',
            'class':'form-control',
            'id':'inputCel',
            'placeholder':'Phone'
        }
    ))
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y',
        attrs={
            'type':'date',
            'class':'form-control',
            'id':'inputDate',
            'placeholder':'Data mm/gg/aaaa'
        }
    ))
    
    
  
    time  =forms.CharField(widget=forms.NumberInput(
         attrs={
             'maxlength':'8',
            'type':'text',
            'class':'form-control',
            'id':'inputTime',
            'placeholder':'Timetables'
         }
    

    ))
    Guests= forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'maxlength':'2',
            'type':'number',
            'class':'form-control',
            'id':'inputNumber',
            'placeholder':'Number of Guests'
        }
    ))

    
    class Meta:
        model=Reserve
        fields=[
            'name',
            'email',
            'phone',
            'date',
            'time',
            'Guests',
        ]