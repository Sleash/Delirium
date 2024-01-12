from django.contrib import admin

# Register your models here.
from .models import Item, Day, Match, Vote

#admin.site.register(Item)
#admin.site.register(Match)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating', 'icon_source')

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('day', 'matches')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('match', 'ip_addr', 'votedA')