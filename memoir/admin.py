from django.contrib import admin
from .models import categories, photos, location


# Register your models here.
admin.site.register([categories, location, photos])
