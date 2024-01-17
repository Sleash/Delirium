from django.contrib import admin

# Register your models here.
from .models import Character, Goal, Streak

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id_int', 'id', 'name', 'icon_source')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id_int', 'id', 'name', 'icon_source')

@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ('character', 'goal', 'player', 'score', 'alive',
                    'vod', 'game_version', 'ebsi', 'optional_comment', 'approved')