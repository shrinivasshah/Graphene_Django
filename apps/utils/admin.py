from django.contrib import admin
from .models import Timestamps
# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ('deck', 'question', 'bucket')


admin.site.register(Timestamps)
