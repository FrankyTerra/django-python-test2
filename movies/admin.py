from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Film, Genre, Country, Comment, Comment2

class MyAdmin(TreeAdmin):
	form = movenodeform_factory(Comment)
	
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Comment, MyAdmin)
admin.site.register(Comment2)
