from Utility.utility_datastructures import DeQueue


class Palindrome:
    try:

        flag = False
        string = input("Enter the string = ")  # To accept the string input
        if len(string) == 1:  # To check if the length of the string is 1 and return true
            flag = True
        else:
            string1 = ""
            # creating a Dequeue object
            deQueue = DeQueue()
            # To add all the characters into the DeQueueLinked list at the rear side
            for i in range(len(string)):
                deQueue.add_rear(string[i])
            # To remove all the characters into the DeQueueLinked list at the front side
            for i in range(len(string)):
                string1 += deQueue.remove_rear()
            if string == string1:
                flag = True
            else:
                flag = False

        if flag:  # To print the result of the string
            print("The given string is a palindrome")
        else:
            print("The given string is not a palindrome")
    except Exception as error:
        print(repr(error))
