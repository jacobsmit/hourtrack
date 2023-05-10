import gspread

sa = gspread.service_account()
sh = sa.open("Hour Track")

wks = sh.worksheet("Tracker")
days = wks.get("C2:AA366")

avg_mood_with_activity = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "total": 0}
sum_mood_with_activity = avg_mood_with_activity.copy()
days_with_activity = avg_mood_with_activity.copy()

for day in days :
    days_with_activity["total"] += 1
    sum_mood_with_activity["total"] += int(day[24])
    counted_activity = {"0": False, "1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "total": False}
    for data in day[:-1] :
        if data in counted_activity and not counted_activity[data] :
            days_with_activity[data] += 1
            sum_mood_with_activity[data] += int(day[24])
            counted_activity[data] = True

print(sum_mood_with_activity)
print(days_with_activity)

for activity in days_with_activity.keys() :
    avg_mood_with_activity[activity] = sum_mood_with_activity[activity] / days_with_activity[activity] / (sum_mood_with_activity["total"] / days_with_activity["total"])

print(avg_mood_with_activity)

