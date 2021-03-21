from django.contrib import admin
from .models import Card
# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ('deck', 'question', 'answer', 'buckets',
                    'bucket', 'next_review_at', 'last_reviewed_at')


admin.site.register(Card, CardAdmin)
