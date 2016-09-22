from django.contrib import admin
from .models import Group
from .models import Person

admin.site.register(Group)
admin.site.register(Person)