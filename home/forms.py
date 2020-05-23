from django import forms
from .models import admin_proses

class FileUplod(forms.ModelForm):
    class Meta:
        model = admin_proses
        fields = ('nama','email','tgl_uplod','file_naskah')
