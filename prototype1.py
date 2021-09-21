##DESCRIPTION IN DIALOG BOX

## Module used ##
import os

## USER INPUTS ##
# n = int(input())  #To get the count of apps
# userInput = {}
# for i in range(n):
#     appName = input()  ##Name of the app
#     permissionList = input().split()  ##List containing all the permissions required by the app
#     userInput[appName] = permissionList

## Hardcoded Input ##
userInput = {
        'B612': ['Camera','Storage'],
        'Whatsapp': ['Camera','Contacts','Microphone','Storage'],
        'Snapchat': ['Camera','Location','Storage'],
        'Teams': ['Calendar','Camera','Microphone'],
        'Truecaller': ['Calling','Contacts','Microphone'],
}

## Dictionary with permission and description as KEY:VALUE pair ##
permissionDesc = {
        'Calendar': "To access device's calendar application for making schedules and reminders for upcoming task, events and meetings.",
        'Camera':"To access device's camera application for capturing pictures and videos.",
        'Contacts':"To access contacts linked to the device for internal functionality of the app.",
        'Location':"To get the track of device's geographic location.",
        'Microphone':"To access the device's in-built microphone for internal functionality of the app.",
        'Calling':"To able to make calls on the device for verification and authentication purpose.",
        'Storage':"To access the internal storage of device for storing the content of the app.",
}

## Description funtion ##
def getDescription(appName):
    #global permissionDesc
    if appName.capitalize() in userInput:
        print("\n\t\t\t",appName," is using these permissions\n")
        for permission in userInput[appName.capitalize()]:
            print("\t",permission," --> ",permissionDesc[permission])
    else:
        print("\n\t",appName," is not installed on your device!!")

    

## Appname function ##
def getAppName(permissionName):
    #global permissionDesc
    if permissionName.capitalize() in permissionDesc:
        print("\n\t\t\t",permissionName," is used by following apps\n")
        for app,permission in userInput.items():
            if permissionName.capitalize() in userInput[app]:
                print("\t--",app,"--")
    else:
        print("\n\tThere is no such app that uses ",permissionName," permission!!")



## OUTPUT ##
print("\n\t\t\t\t##WELCOME TO PERMISSION CHECK!! ##")
print("\n")

print("\tThese are the services provided by our Application")

counter = True

while counter:
    print("\n\t1. Get to know about the permissions your apps are taking from you!")
    print("\t2. Get to know which apps are using a permission!")
    print("\t3. Exit the application!")
    print()
    ch = int(input("\tChoose the service count : "))

    if ch==1:
        appName = input("\n\tEnter the App name: ")
        getDescription(appName)

    elif ch==2:
        permission = input("\n\tEnter the permission name: ")
        getAppName(permission)

    elif ch==3:
        counter = False
        break

    else:
        print("\n\tYou may have entered an invalid choice..")
        print("\tTry Again!!")
        continue

os.system('cls')
print("\n\tThank you for using our Application!!")
print("\tIf you liked our App, please rate us on playstore!!")
