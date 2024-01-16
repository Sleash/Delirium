from datetime import datetime, timezone
import random

from django.db import models
from django.db.models import F

from .utils import datetimeToIdMatch, timeToMatchNumber

# Create your models here.

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    icon_source = models.CharField(max_length=100)
    rating = models.IntegerField(default=1000)

    class Meta:
        ordering = ['-rating', 'id']
    
    def __str__(self):
        return self.name

 
class Day(models.Model):
    day = models.DateField(auto_now_add=True, primary_key=True)
    matches = models.JSONField()

    class Meta:
        ordering = ['-day']
    
    @classmethod
    def create(cls): # create new day with random permutation of all items
        allItems = [i.id for i in Item.objects.all()]
        random.shuffle(allItems)
        day = cls(matches=allItems)
        day.save()
        return day
    
    def getItems(self, n: int): # n = matchNumber
        firstitem = 2*(n-1) # 1 2 3 ... 360 -> 0 2 4 ... 718
        seconditem = firstitem + 1 # 1 3 5 ... 719
        return (self.matches[firstitem], self.matches[seconditem])
    
    @staticmethod
    def getItemsForNewMatch(now: datetime):
        query = Day.objects.filter(day=now.date())
        if not query.exists(): # Day does not exist yet
            da = Day.create()
        else:
            da = query.first()
        matchNumber = timeToMatchNumber(now.time())
        return da.getItems(matchNumber)

RATING_RATIO = 480
K_FACTOR = 32

class Match(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemA = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="itemA")
    itemB = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="itemB")
    scoreA = models.IntegerField(default=0)
    scoreB = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{0} ({1}) VS ({2}) {3} [{4}]'.format(
            self.itemA.name, self.scoreA, self.scoreB, self.itemB.name, self.id)
    
    @classmethod
    def create(cls, idm: int, now: datetime):
        (A, B) = Day.getItemsForNewMatch(now)
        m = cls(id=idm,
                itemA=Item.objects.get(id=A),
                itemB=Item.objects.get(id=B))
        m.save()
        return m
    
    @classmethod
    def getCurrent(cls):
        now = datetime.now(timezone.utc)
        idm = datetimeToIdMatch(now)
        m = Match.objects.first()
        if idm != m.id : # Match does not exist yet
            # Resolve previous match
            m.fulfill()
            # then create the new one
            m = Match.create(idm, now)
        return m
    
    def vote(self, ip_addr, vote):
        v = Vote(ip_addr=ip_addr,match=self,votedA= (vote == 'A') )
        v.save()
        if vote == 'A':
            self.scoreA = F("scoreA") + 1
            self.save(update_fields=["scoreA"])
        if vote == 'B':
            self.scoreB = F("scoreB") + 1
            self.save(update_fields=["scoreB"])
        self.refresh_from_db()

    def fulfill(self):
        # No votes special case
        if self.scoreA + self.scoreB == 0:
            return

        Qa = pow(10, self.itemA.rating/RATING_RATIO)
        Qb = pow(10, self.itemB.rating/RATING_RATIO)

        # Expected scores for A and B
        Ea = Qa/(Qa+Qb)
        Eb = Qb/(Qa+Qb)

        # Actual scores for A and B
        Sa = self.scoreA/(self.scoreA+self.scoreB)
        Sb = self.scoreB/(self.scoreA+self.scoreB)

        # Updating ratings for A and B
        self.itemA.rating = F("rating") + round( K_FACTOR * (Sa - Ea) )
        self.itemB.rating = F("rating") + round( K_FACTOR * (Sb - Eb) )
        self.itemA.save(update_fields=["rating"])
        self.itemB.save(update_fields=["rating"])

class Vote(models.Model):
    ip_addr = models.CharField(max_length=15)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    votedA = models.BooleanField() # vote = B if false

    class Meta:
        ordering = ['match', 'ip_addr']

    def getVote(self):
        return 'A' if self.votedA else 'B'