from datetime import datetime
from datetime import timedelta

curr = datetime.strptime(input(), "%H:%M:%S")
explosion = datetime.strptime(input(), "%H:%M:%S")

if (curr == explosion):
    print("24:00:00")
    exit()

delta = explosion - curr
if curr > explosion:
    delta += timedelta(days=1)
delta = str(delta)
print("0" + delta if len(delta) == 7 else delta)
