import pprint
import birthdayList


def enter():
    print("Enter name")
    name = input()
    print("Enter birthday in format d/m/y")
    date = input()
    print("Enter email")
    email = input()
    day = int(date[0]) * 10 + int(date[1])
    month = int(date[3]) * 10 + int(date[4])
    year = int(date[6]) * 1000 + int(date[7]) * 100 + int(date[8]) * 10 + int(date[9])
    tempDictionary = {"name": name, "date": [day, month, year], "email": email}
    birthdayList.birthdayList.append(tempDictionary)
    fileBirthdayList = open("birthdayList.py", "w")
    fileBirthdayList.write("birthdayList = " + pprint.pformat(birthdayList.birthdayList))
    fileBirthdayList.close()

def delete():
    tempDictionary = birthdayList.birthdayList
    print("Delete by name? (y/n)")
    deleteChoice = "m"
    while (deleteChoice != "y") and (deleteChoice != "n"):
        deleteChoice = input()
    if deleteChoice == "y":
        print("Enter the name you wish to delete")
        inputName = input()
        for i in range(0, len(tempDictionary)):
            if tempDictionary[i]["name"].lower() == inputName.lower():
                del tempDictionary[i]
                fileBirthdayList = open("birthdayList.py", "w")
                fileBirthdayList.write("birthdayList = " + pprint.pformat(tempDictionary))
                fileBirthdayList.close()
                break

    elif deleteChoice == "n":
        print("Enter index of the entry you want to delete")
        indexInput = int(input())
        if indexInput > len(tempDictionary):
            print("Index out of bounds!")
        else:
            del tempDictionary[indexInput - 1]
            fileBirthdayList = open("birthdayList.py", "w")
            fileBirthdayList.write("birthdayList = " + pprint.pformat(tempDictionary))
            fileBirthdayList.close()


def view():
    counter = 0
    for entry in birthdayList.birthdayList:
        counter += 1
        print("Index: " + str(counter) + "\tName: " + entry["name"] + "\t\tDate: " + str(entry["date"][0]) + "/" + str(entry["date"][1]) + "/" + str(entry["date"][2]) + "\t\tE-mail: " + entry["email"])



#Main
choice = -1

while True:
    print()
    print("1) New Entry")
    print("2) Delete")
    print("3) View")
    print("4) Quit!")

    choice = int(input())

    if choice == 1:
        enter()

    if choice == 2:
        delete()

    if choice == 3:
        view()

    if choice == 4:
        break

