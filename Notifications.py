from datetime import datetime

today = datetime.today().strftime("%d/%m/%Y")
today = datetime.strptime(today, "%d/%m/%Y")
class Notification: 
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
notifications = []

def add_notification(name, date):
    notification = Notification(name, date)
    notifications.append(notification)
    
add_notification("Yesterday", "21/05/2026")
add_notification("Today", "22/05/2026")
add_notification("Tomorrow", "23/05/2026")
add_notification("In 15 days", "06/06/2026")
add_notification("In 30 days", "21/06/2026")
add_notification("In 31 days", "22/06/2026")

for i in range(len(notifications)):
    print(i)
    calc = datetime.strptime(notifications[i].date, "%d/%m/%Y") - today
    if  calc.days <= 30 and calc.days >= 0:print(f"This notifications expires over the next 30 days:\n {notifications[i].name}\n {notifications[i].date}\n")
