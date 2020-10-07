from django.contrib import admin

from .models import ObjectType
from .models import Object


admin.site.register(ObjectType)
admin.site.register(Object)