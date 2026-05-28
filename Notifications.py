from datetime import datetime
from Lib import json
from desktop_notifier import DesktopNotifier, Button, DEFAULT_SOUND
import asyncio

today = datetime.strptime("22/05/2026", "%d/%m/%Y") #datetime.today().strftime("%d/%m/%Y")
menu = ""
class Notification: 
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
notifications = []
notifier = DesktopNotifier(app_name="Notifications py")

def validate_date():
    try:
        date = input("Enter the date (dd/mm/yyyy): ")
        if going_back(date) == True:
            return "back"
        else:
            validated_date = datetime.strptime(date, "%d/%m/%Y")
            return validated_date.strftime("%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in dd/mm/yyyy format.")
        return validate_date()

def add_notification(name, date):
    notification = Notification(name, date)
    notifications.append(notification)
    
def input_notifications():
    print("Add a notification")
    print("Type 'back', 'b' or leave empty to go back.")
    name = input("Enter the name of the notification: ")
    if going_back(name) == True:
        return
    date = validate_date()
    if date == "back":
        return
    add_notification(name, date)
    print("Notification added successfully.")
    going_back(input("Press Enter to go back..."))
    
def list_notifications():
    print("List of notifications:")
    for notification in notifications:
        print(f"Name: {notification.name}, Date: {notification.date}")
    going_back(input("Press Enter to go back..."))

def search_notification(name):
    for i in range(len(notifications)):
        if notifications[i].name == name:
            return i
    return -1 
     
def edit_notification():
    print("Edit a notification")
    print("Type 'back', 'b' or leave empty to go back.")
    name = input("Enter the name of the notification to edit: ")
    if going_back(name) == True:
        return
    index = search_notification(name)
    if index != -1:
        print(f"Name: {notifications[index].name}, Date: {notifications[index].date}")
        confirm = input("Are you sure you want to edit this notification? (y/n): ")
        if confirm.lower() == "y":
            new_name = input("Enter the new name of the notification: ")
            new_date = validate_date()
            notifications[index].name = new_name
            notifications[index].date = new_date
            print("Notification edited successfully.")
        elif confirm.lower() == "n":
            print("Edit cancelled.")
            going_back(input("Press Enter to go back..."))
    else:
        print("Notification not found.")
    
def delete_notification():
    print("Delete a notification")
    print("Type 'back', 'b' or leave empty to go back.")
    name = input("Enter the name of the notification to delete: ")
    if going_back(name) == True:
        return
    index = search_notification(name)
    if index != -1:
        print(f"Name: {notifications[index].name}, Date: {notifications[index].date}")
        confirm = input("Are you sure you want to delete this notification? (y/n): ")
        if confirm.lower() == "y":
            del notifications[index]
            print("Notification deleted successfully.")
        elif confirm.lower() == "n":
            print("Deletion cancelled.")
            going_back(input("Press Enter to go back..."))        
    else:
        clear()
        print("Notification not found.")
        return delete_notification()

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
           
def check_expiring_notifications():
    print("Check expiring notifications")
    print("Type 'back', 'b' or leave empty to go back.")
    expiring = input("number of days till expiration:")
    if going_back(expiring) == True:
        return
    try:
        expiring = int(expiring)
    except ValueError:
        clear()
        print("Invalid input. Please enter a valid number.")
        return check_expiring_notifications()
    print(f"Notifications expiring in the next {expiring} days:")
    for i in range(len(notifications)):
        calc = datetime.strptime(notifications[i].date, "%d/%m/%Y") - today
        if  calc.days <= expiring and calc.days >= 0:
            #windows_notification(i)
            console_notification(i)
    going_back(input("Press Enter to go back..."))
           
def open_data():
    try: 
        with open('data.json', 'r') as file:
            data = json.load(file)
        for item in data:
            add_notification(item['name'], item['date'])
    except FileNotFoundError:
        print("No existing data found.")

def saving_data():
    with open('data.json', 'w') as file:
        newdata = []
        for notification in notifications:
            newdata.append({"name": notification.name, "date": notification.date})
        file.write(json.dumps(newdata, indent=4))    

def clear():
    print("\033[H\033[J", end="")

def going_back(string):
    if string.lower() == "back" or string.lower() == "b" or string == "":
        return True
    return False

open_data()    

while menu != "0":
    clear()
    print(
        "Notifications:\n"
        "1 - Add a notification\n"
        "2 - List notifications\n"
        "3 - Edit a notification\n"
        "4 - Delete a notification\n"
        "5 - Check expiring notifications\n"
        "0 - Exit"
        )
    menu = input("Enter your choice: ")
    if menu == "1":
        clear()
        input_notifications()
    elif menu == "2":
        clear()
        list_notifications()
    elif menu == "3":
        clear()
        edit_notification()      
    elif menu == "4":
        clear()
        delete_notification()
    elif menu == "5":
        clear()
        check_expiring_notifications()    
    elif menu == "0":
        print("Exiting...")      
saving_data()

