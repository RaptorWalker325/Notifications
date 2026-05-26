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
   
#load from json file    
with open('data.json', 'r') as file:
    data = json.load(file)
for item in data:
    add_notification(item['name'], item['date'])

add = input("Do you want to add a notification? (y/n) ")
if add == "y":
    name = input("Enter the name of the notification: ")
    date = input("Enter the date of the notification (dd/mm/yyyy): ")
    add_notification(name, date)

for i in range(len(notifications)):
    calc = datetime.strptime(notifications[i].date, "%d/%m/%Y") - today
    if  calc.days <= 30 and calc.days >= 0:print(f"This notifications expires over the next 30 days:\n {notifications[i].name}\n {notifications[i].date}\n")

#write to json file
with open('data.json', 'w') as file:
    newdata = []
    for notification in notifications:
        newdata.append({"name": notification.name, "date": notification.date})
    json_string = json.dumps(newdata, indent=4)
    file.write(json_string)