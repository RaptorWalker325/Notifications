from datetime import datetime
from Lib import json

today = "22/05/2026" #datetime.today().strftime("%d/%m/%Y")
today = datetime.strptime(today, "%d/%m/%Y")
menu = ""
class Notification: 
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
notifications = []

def add_notification(name, date):
    notification = Notification(name, date)
    notifications.append(notification)
    
def input_notifications():
    name = input("Enter the name of the notification: ")
    date = input("Enter the date of the notification (dd/mm/yyyy): ")
    add_notification(name, date)
    
def list_notifications():
    for notification in notifications:
        print(f"Name: {notification.name}, Date: {notification.date}")

def search_notification(name):
    for i in range(len(notifications)):
        if notifications[i].name == name:
            return i
    return -1      
def edit_notification(index, name, date):
    notifications[index].name = name
    notifications[index].date = date
    
def delete_notification(index):
    del notifications[index]        
#load from json file    
with open('data.json', 'r') as file:
    data = json.load(file)
for item in data:
    add_notification(item['name'], item['date'])
    
while menu != "0":
    print("Notifications:\n 1 - Add a notification\n 2 - List notifications\n 3 - Edit a notification \n 4 - Delete a notification\n 0 - Exit")
    menu = input("Enter your choice: ")
    if menu == "1":
        input_notifications()
    elif menu == "2":
        list_notifications()
    elif menu == "3":
        name = input("Enter the name of the notification to edit: ")
        index = search_notification(name)
        if index != -1:
            new_name = input("Enter the new name of the notification: ")
            new_date = input("Enter the new date of the notification (dd/mm/yyyy): ")
            edit_notification(index, new_name, new_date)
        else:
            print("Notification not found.")
    elif menu == "4":
        name = input("Enter the name of the notification to delete: ")
        index = search_notification(name)
        if index != -1:
            delete_notification(index)
        else:
            print("Notification not found.")        
    elif menu == "0":
        print("Exiting...")        

print("Notifications expiring in the next 30 days:")
for i in range(len(notifications)):
    calc = datetime.strptime(notifications[i].date, "%d/%m/%Y") - today
    if  calc.days <= 30 and calc.days >= 0:print(f"{notifications[i].name}\n{notifications[i].date}\n")

#write to json file
with open('data.json', 'w') as file:
    newdata = []
    for notification in notifications:
        newdata.append({"name": notification.name, "date": notification.date})
    json_string = json.dumps(newdata, indent=4)
    file.write(json_string)