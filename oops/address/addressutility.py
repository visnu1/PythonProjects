from ObjectOrientedPrograms.addresBook import addressBookInterface, person, address


class AddrressUtility(addressBookInterface.AddressBook):

    def __init__(self):
        self.list = []

    def add(self):
        firstname = input("Enter firstname: ")
        lastname = input("Enter lastname: ")

        city = input("Enter city")

        zip = input("Enter zip")

        state = input("Enter state")

        phone = input("Enter phonenumber")
        addre = address.Address(city, zip, state, phone)
        per = person.Person(firstname, lastname, addre)
        self.list.append(per)

    def edit(self):

        firstname = input("Enter Person FirstName Of Edited Person")
        phone = print("Enter MobileNumber Of Edited Person")
        for i in self.list:
          temp=self.list.append(i)
        if temp.get_first_name.equals(firstname) and temp.get_address.get_phone().equals(phone):
            print("What You Want To Edit")
            print("1.LastName")
            print("2.City")
            print("3.Zip")
            print("4.State")
            print("5.Phone")
            print("6.Exit")
            Answer2 = input("Enter your choice")
        if Answer2 == 1:
            lastname = input("Enter the lastname :")
            self.list.get(i).set_last_name(lastname)
        elif Answer2 == 2:
            city = input("Enter New City :")
            self.list.get(i).set_city = city
        elif Answer2 == 3:
            zip = input("Enter New Zip :")
            self.list.get(i).address.zip = zip
        elif Answer2 == 4:
            state = input("Enter New State :")
            self.list.get(i).set_state = state
        elif Answer2 == 5:
            phone = input("Enter New Phone :")
            list.get(i).set_phone = phone
        elif Answer2 == 6:
            print("Exiting")

        else:
            print("Invalid Entry")

        if (i > list.size()):
            print("No Person Found With This Details")
