# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:47:53 2022

@author: watson
"""

from django import forms
from .models import Photo

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control-file'})
            }