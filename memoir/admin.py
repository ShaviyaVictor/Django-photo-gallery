from django.contrib import admin
from .models import categories, photos


# Register your models here.
admin.site.register([categories, photos])
