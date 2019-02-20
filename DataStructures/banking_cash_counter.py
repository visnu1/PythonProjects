"""
# ******************************************************************************

#  Purpose        : To simulate a banking system where in checks if the bank
#                   has maintained a proper balance at the end of the day
#  @file          : banking_cash_counter.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 17/02/2019

# ******************************************************************************
"""
from Utility.utility_datastructures import Queue

import math


class BankingCashCounter:
    try:
        # instantiating two queue objects for name and amount
        queue1 = Queue()
        queue2 = Queue()
        bank_amount = int(input("Enter the amount in the bank = "))  # The amount in the bank
        min_bank_balance = 2000  # The minimum balance
        customers = int(math.fabs(int(input(
            "Enter the no of people to be given service = "))))  # To get the number of customers to be given service
        for i in range(customers):  # Loop for the desired number of customers
            customer_name = input("Enter your name = ")  # Accepting the customer name
            queue1.en_queue(customer_name)  # adding all the names into the queue
            choice = int(input("Enter your choice \n\t1.Deposit: \n\t2.Withdraw:"))
            while True:  # Input validation
                if choice is 1 or choice is 2:
                    break
                choice = int(input("Enter a correct choice: "))
            amount = int(input("Enter the amount = "))  # To get the amount from the customer
            queue2.en_queue({choice: amount})  # To push all the customer amount details

        while not queue2.is_empty():  # Loop until the queue is empty

            dict = queue2.de_queue()
            if 1 in dict:  # Accessing the details from the dictionary and perform the necessary transactions
                print("Dear, ", str(queue1.de_queue()), " you have successfully deposited", str(dict[1]))
                bank_amount += dict[1]

            else:  # for amount withdraw
                print("Dear, ", str(queue1.de_queue()), " you have successfully withdrew ", str(dict[2]))
                bank_amount -= dict[2]

        if bank_amount < min_bank_balance:  # To check the bank balance with the min. balance
            print("Bank balance not maintained = ", str(bank_amount))
        else:
            print("Bank balance maintained = ", str(bank_amount))

    except Exception as error:
        print(repr(error))
