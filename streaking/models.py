from django.db import models

class Character(models.Model):
    id = models.CharField(max_length=10)
    id_int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    icon_source = models.CharField(max_length=100)

    class Meta:
        ordering = ['id_int']

    def __str__(self):
        return self.name

    @staticmethod
    def initCharacters():
        CHARACTERS = {
            'all': ('All', '4/4b/MainPageChallenges.png/revision/latest?cb=20141129224206'),

            'isaac': ('Isaac', 'e/e5/Character_Isaac_appearance.png/revision/latest?cb=20231008190524'),
            'magdalene': ('Magdalene', 'b/bf/Character_Magdalene_appearance.png/revision/latest?cb=20210824111834'),
            'cain': ('Cain', 'd/db/Character_Cain_appearance.png/revision/latest?cb=20211204211028'),
            'judas': ('Judas', '8/8d/Character_Judas_appearance.png/revision/latest?cb=20210826071249'), # 12 is Dark Judas
            'bluebaby': ('???', '9/9a/Character_%3F%3F%3F_appearance.png/revision/latest?cb=20210824125207'),
            'eve': ('Eve', '9/91/Character_Eve_appearance.png/revision/latest?cb=20210826071757'),
            'samson': ('Samson', '8/8c/Character_Samson_appearance.png/revision/latest?cb=20210824125143'),
            'azazel': ('Azazel', '0/06/Character_Azazel_appearance.png/revision/latest?cb=20210824125228'),
            'lazarus': ('Lazarus', '7/78/Character_Lazarus_appearance.png/revision/latest?cb=20211111110428'), # 11 is Lazarus Risen
            'eden': ('Eden', '8/83/Character_Eden_appearance.png/revision/latest?cb=20210826072021'),
            'lost': ('The Lost', 'f/f0/Character_The_Lost_appearance.png/revision/latest?cb=20210826071932'),
            'lilith': ('Lilith', 'a/a8/Character_Lilith_appearance.png/revision/latest?cb=20210821134536'),
            'keeper': ('Keeper', '2/20/Character_Keeper_appearance.png/revision/latest?cb=20210821185529'),
            'apollyon': ('Apollyon', '4/40/Character_Apollyon_appearance.png/revision/latest?cb=20210822021832'),
            'forgotten': ('The Forgotten', '2/21/Character_The_Forgotten_appearance.png/revision/latest?cb=20210822091711'), # 17 is The Soul
            'bethany': ('Bethany', '8/82/Character_Bethany_appearance.png/revision/latest?cb=20210822150024'),
            'jacobesau': ('Jacob & Esau', '1/1d/Character_Jacob_and_Esau_appearance.png/revision/latest?cb=20210824111920'), # 20 is Esau

            'rrandom': ('Regular Random', '4/4b/Collectible_Clicker_icon.png/revision/latest?cb=20210822014653'),

            'tisaac': ('Tainted Isaac', 'e/ec/Character_Tainted_Isaac_appearance.png/revision/latest?cb=20210824112002'),
            'tmagdalene': ('Tainted Magdalene', 'f/f1/Character_Tainted_Magdalene_appearance.png/revision/latest?cb=20210824112024'),
            'tcain': ('Tainted Cain', '2/2e/Tainted_Cain_App.png/revision/latest?cb=20210825173304'),
            'tjudas': ('Tainted Judas', '0/0e/Tainted_Judas_App.png/revision/latest?cb=20210825173324'),
            'tbluebaby': ('Tainted ???', 'c/c1/Tainted_Blue_Baby_App.png/revision/latest?cb=20210825173344'),
            'teve': ('Tainted Eve', '0/04/Tainted_Eve_App.png/revision/latest?cb=20210825173404'),
            'tsamson': ('Tainted Samson', '7/72/Tainted_Samson_App.png/revision/latest?cb=20210825173424'),
            'tazazel': ('Tainted Azazel', '6/61/Tainted_Azazel_App.png/revision/latest?cb=20210825173445'),
            'tlazarus': ('Tainted Lazarus', '7/70/Character_Tainted_Lazarus_appearance.png/revision/latest?cb=20230111000758'), # 38 is Dead Tainted Lazarus
            'teden': ('Tainted Eden', '5/57/Character_Tainted_Eden_appearance.png/revision/latest?cb=20210824112436'),
            'tlost': ('Tainted Lost', 'b/b7/Tainted_Lost_App.png/revision/latest?cb=20210825173525'),
            'tlilith': ('Tainted Lilith', 'a/a7/Tainted_Lilith_App.png/revision/latest?cb=20210825173545'),
            'tkeeper': ('Tainted Keeper', '0/05/Tainted_Keeper_App.png/revision/latest?cb=20210825173606'),
            'tapollyon': ('Tainted Apollyon', '2/27/Tainted_Apollyon_App.png/revision/latest?cb=20210825173626'),
            'tforgotten': ('Tainted Forgotten', '1/1f/Character_Tainted_Forgotten_appearance.png/revision/latest?cb=20210824112044'), # 40 is Tainted Soul
            'tbethany': ('Tainted Bethany', 'e/ed/Tainted_Bethany_App.png/revision/latest?cb=20210825173646'),
            'tjacob': ('Tainted Jacob', '0/0b/Tainted_Jacob_App.png/revision/latest?cb=20210825173706'), # 39 is Lost Jacob
            
            'trandom': ('Tainted Random', '4/4b/Collectible_Clicker_icon.png/revision/latest?cb=20210822014653'),
        }
        for c, d in CHARACTERS.items():
            Character(id=c, name=d[0], icon_source=d[1]).save()

class Goal(models.Model):
    id = models.CharField(max_length=10)
    id_int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    icon_source = models.CharField(max_length=100)

    class Meta:
        ordering = ['id_int']

    def __str__(self):
        return self.name

    @staticmethod
    def initGoals():
        GOALS = {
            'all': ('All', '4/4b/MainPageChallenges.png/revision/latest?cb=20141129224206'),

            'fourgoals': ('Four Goals', 'e/e0/Stage_The_Void_room.png/revision/latest/scale-to-width-down/270?cb=20210825082639'),
            'bluebaby': ('???', 'b/b8/Boss_%3F%3F%3F_portrait.png/revision/latest?cb=20210409161656'),
            'lamb': ('The Lamb', 'c/cc/Boss_The_Lamb_portrait.png/revision/latest?cb=20210821071710'),
            'mother': ('Mother', '8/8a/Boss_Mother_portrait.png/revision/latest?cb=20210824103236'),
            'beast': ('The Beast', '3/37/Boss_The_Beast_ingame.png/revision/latest?cb=20210824113546'),
            'greedier': ('Ultra Greedier', '0/0d/Boss_Ultra_Greedier_ingame.png/revision/latest?cb=20190328084436'),
            'megasatan': ('Mega Satan', '8/80/Boss_Mega_Satan_portrait.png/revision/latest?cb=20210414134726'),
            'delirium': ('Delirium', 'd/df/Boss_Delirium_portrait.png/revision/latest?cb=20210409161216'),
        }
        for g, h in GOALS.items():
            Goal(id=g, name=h[0], icon_source=h[1]).save()

# Create your models here.
class Streak(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    goal = models.ForeignKey(Goal, on_delete=models.PROTECT)
    player = models.CharField(max_length=50)
    score = models.IntegerField()
    alive = models.BooleanField()
    gameVersion = models.CharField(max_length=50, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-score', '-alive']