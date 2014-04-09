#!/usr/bin/env python
# coding=utf-8
from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(widget=forms.Textarea)
    priority = forms.RadioInput()
