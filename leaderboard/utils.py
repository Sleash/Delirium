from datetime import datetime, date, time

MATCH_DURATION_MINUTES = 4

def timeToMatchNumber(time: time):
    totalMinutes = 60*time.hour + time.minute
    # match number between 1 and 360
    matchNumber = totalMinutes//MATCH_DURATION_MINUTES +1
    return matchNumber

def matchNumberToTime(matchNumber: int):
    totalMinutes = (matchNumber-1)*MATCH_DURATION_MINUTES
    return time(totalMinutes//60, totalMinutes%60)

def datetimeToIdMatch(d: datetime):
    id = d.year
    id = id*100 + d.month
    id = id*100 + d.day
    id = id*1000 + timeToMatchNumber(d.time())
    return id

def idMatchToDatetime(id: int):
    (id, matchNumber) = divmod(id, 1000)
    (id, day) = divmod(id, 100)
    (year, month) = divmod(id, 100)
    return datetime.combine(date(year, month, day), matchNumberToTime(matchNumber) )
