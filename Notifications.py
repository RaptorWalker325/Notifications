from datetime import datetime

from Lib import json

today = "22/05/2026" #datetime.today().strftime("%d/%m/%Y")
today = datetime.strptime(today, "%d/%m/%Y")
class Notification: 
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
notifications = []

def add_notification(name, date):
    notification = Notification(name, date)
    notifications.append(notification)
    
with open('data.json', 'r') as file:
    data = json.load(file)
for item in data:
    add_notification(item['name'], item['date'])

for i in range(len(notifications)):
    calc = datetime.strptime(notifications[i].date, "%d/%m/%Y") - today
    if  calc.days <= 30 and calc.days >= 0:print(f"This notifications expires over the next 30 days:\n {notifications[i].name}\n {notifications[i].date}\n")

