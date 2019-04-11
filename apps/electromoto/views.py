#/home/greenhub/django/django_env/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	return render(request, 'electromoto/base_electromoto.html')
