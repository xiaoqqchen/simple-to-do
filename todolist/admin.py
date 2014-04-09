#!/usr/bin/env python
# coding=utf-8

from django.contrib import admin
from todolist.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('user','todo','priority','flag','pubtime')
    list_fliter = ('pubtime',)
    ordering=('-pubtime',)


admin.site.register(Todo,TodoAdmin)

