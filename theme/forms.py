# -*- coding: utf-8 -*-
from django import forms

class AddThemeForm(forms.Form):
    title       = forms.CharField(max_length=250)
    description = forms.CharField(max_length=500)
