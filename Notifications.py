from datetime import datetime
from Lib import json
from desktop_notifier import DesktopNotifier, Button, DEFAULT_SOUND
import asyncio

today = "22/05/2026" #datetime.today().strftime("%d/%m/%Y")
today = datetime.strptime(today, "%d/%m/%Y")
menu = ""
class Notification: 
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
notifications = []
notifier = DesktopNotifier(app_name="Notifications py")

def add_notification(name, date):
    notification = Notification(name, date)
    notifications.append(notification)
    
def input_notifications():
    name = input("Enter the name of the notification: ")
    date = input("Enter the date of the notification (dd/mm/yyyy): ")
    add_notification(name, date)
    print("Notification added successfully.")
    
def list_notifications():
    for notification in notifications:
        print(f"Name: {notification.name}, Date: {notification.date}")

def search_notification(name):
    for i in range(len(notifications)):
        if notifications[i].name == name:
            return i
    return -1 
     
def edit_notification():
    name = input("Enter the name of the notification to edit: ")
    index = search_notification(name)
    if index != -1:
            new_name = input("Enter the new name of the notification: ")
            new_date = input("Enter the new date of the notification (dd/mm/yyyy): ")
            notifications[index].name = new_name
            notifications[index].date = new_date
    else:
            print("Notification not found.")
    
def delete_notification():
    name = input("Enter the name of the notification to delete: ")
    index = search_notification(name)
    if index != -1:
        del notifications[index]
    else:
        print("Notification not found.")  

def windows_notification(i):
    async def main():
            await notifier.send(
                title="Expiring in 30 days",
                message=f"{notifications[i].name} is expiring on {notifications[i].date}",
                buttons=[
                     Button(
                title="Mark as read",
                on_pressed=lambda: print("Marked as read"),
                            )
                ],
                sound=DEFAULT_SOUND
            )
    asyncio.run(main())        

def console_notification(i):
    print(f"{notifications[i].name} is expiring on {notifications[i].date}")
           
def check_expiring_notifications(expiring):
    print(f"Notifications expiring in the next {expiring} days:")
    for i in range(len(notifications)):
        calc = datetime.strptime(notifications[i].date, "%d/%m/%Y") - today
        if  calc.days <= expiring and calc.days >= 0:
            #windows_notification(i)
            console_notification(i)
           
def opendata(): 
    with open('data.json', 'r') as file:
        data = json.load(file)
    for item in data:
        add_notification(item['name'], item['date'])

def savingdata():
    with open('data.json', 'w') as file:
        newdata = []
        for notification in notifications:
            newdata.append({"name": notification.name, "date": notification.date})
        file.write(json.dumps(newdata, indent=4))    

opendata()    
while menu != "0":
    print("Notifications:\n 1 - Add a notification\n 2 - List notifications\n 3 - Edit a notification \n 4 - Delete a notification\n 5 - Check expiring notifications\n 0 - Exit")
    menu = input("Enter your choice: ")
    if menu == "1":
        input_notifications()
    elif menu == "2":
        list_notifications()
    elif menu == "3":
        edit_notification()        
    elif menu == "4":
        delete_notification()
    elif menu == "5":
        expiring = int(input("check notifications for expiring in the next: "))
        check_expiring_notifications(expiring)
    elif menu == "0":
        print("Exiting...")        
savingdata()
        
        

