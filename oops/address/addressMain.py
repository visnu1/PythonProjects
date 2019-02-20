from ObjectOrientedPrograms.addresBook import addressutility

manager = addressutility.AddrressUtility()


class AddressBookApplication:
    while True:
        print("Welcome To Address Book")
        print("Choose Operation You Want To Do")
        print("1.Add")
        print("2.Open")
        print("3.Save")
        print("4.SaveAs")
        print("5.Close")
        print("6.Exit")
        answer = int(input("Enter the choice: "))
        switcher = {1: manager.add(), 2: manager.edit()}
        if answer is 6:
            break

