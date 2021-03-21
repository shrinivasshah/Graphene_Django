from django.contrib import admin
from .models import Deck
# Register your models here.


class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'last_reviewed')


admin.site.register(Deck, DeckAdmin)
