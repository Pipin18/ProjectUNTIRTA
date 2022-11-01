from dataclasses import fields
from django.forms import ModelForm
from django import forms
from tendik.models import Tendik

class FormTendik(ModelForm):
    class Meta:
        model = Tendik
        exclude = ['tambah-tendik']

        widgets = {
            'no' : forms.TextInput ({'class':'form-control'}),
            'nama' : forms.TextInput ({'class':'form-control'}),
            'nip' : forms.TextInput ({'class':'form-control'}),
            'jabatan' : forms.TextInput ({'class':'form-control'}),
        }
        