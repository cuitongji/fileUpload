# /usr/bin/python
# -*- coding: utf-8 -*-

from django import forms


class UserForm(forms.Form):
	uname = forms.CharField(max_length=20)
	uploadFile = forms.FileField()
